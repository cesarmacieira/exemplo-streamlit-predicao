import streamlit as st
import pandas as pd
import numpy as np
from Funcoes import DescritivaCat, DescritivaNum
from Funcoes import Descritiva1Num1Cat, DescritivaVarNum1Cat
from Funcoes import Comparações1VarCat1VarCat, Comparações1VarNum1VarCat
import plotly.express as px
from PIL import Image
st.set_page_config(
        page_title="Aplicativo",#Nome da página no chrome
        page_icon="📊",#Emoji⚙️🏠📈📊🖥️
        layout="wide" #identifica se é a página inteira
    ) 

st.title('Análise descritiva')

dados = pd.read_excel("Dados completos.xlsx", sheet_name='Sheet1')

def DescritivaCat(df, cols):
    frames = []
    for col in cols:
        frame = df.groupby([col], observed=True).size().reset_index(name='Freq. Absoluta (N)')
        frame['Freq. Relativa (%)'] = frame['Freq. Absoluta (N)'] / len(df) * 100
        frame.insert(0, 'Variável', col)
        frame = frame.rename(columns={col: 'Categoria'})
        if not frame.empty:
            frames.append(frame)
    result = pd.concat(frames, ignore_index=True)
    return result

variaveis = ['LE','ESP_ENSAIO_TR','LARG','C','AL','DESENF','ACAB','BOB']
variaveis_categoricas = ['TIPO_CP', 'REV']

graf1, graf2 = st.columns([1, 1])
with graf1:
    selected_variavel = st.selectbox('Selecione a variável numérica:', variaveis)
    fig = px.box(dados, x='STATUS', y=selected_variavel, color='STATUS',
                title=f'{selected_variavel}')
    for i, cor in enumerate(['#0000FF', '#FF0000']):
        fig.data[i].marker.color = cor
    #fig.update_layout(xaxis_title='STATUS', yaxis_title=selected_variavel, title_x=0.4, width=570, height=500)
    fig.update_layout(xaxis_title='STATUS', yaxis_title=selected_variavel, width=570, height=500)
    st.plotly_chart(fig)
with graf2:
    selected_variavel = st.selectbox('Selecione a variável categórica:', variaveis_categoricas)
    data_grouped = dados.groupby(['STATUS', selected_variavel]).size().reset_index(name='COUNT')
    data_grouped['PERCENT'] = (data_grouped['COUNT'] / data_grouped.groupby('STATUS')['COUNT'].transform('sum')) * 100
    fig = px.bar(data_grouped, x=selected_variavel, y='PERCENT', color='STATUS',
             title=f'{selected_variavel}',
             color_discrete_sequence=['blue', 'red'])
    fig.update_layout(xaxis_title=selected_variavel, yaxis_title='Percentual (%)', barmode='group', width=570, height=500)
    st.plotly_chart(fig)

desc1, desc2 = st.columns([1.8,1])
with desc1:
    st.write(DescritivaNum(dados, ['LE','ESP_ENSAIO_TR','LARG','C','AL','DESENF','ACAB','BOB']).round(1))
with desc2:
    st.write(DescritivaCat(dados, ['STATUS','TIPO_CP','REV']))
print(dados.head)

ver_dados = st.button('Ver dados completos')
if ver_dados:
    st.dataframe(dados)