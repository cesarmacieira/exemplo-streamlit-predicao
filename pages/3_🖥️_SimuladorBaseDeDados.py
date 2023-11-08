import streamlit as st
import pickle
import bz2
import pandas as pd
import xgboost as xgb
import time

st.set_page_config(
        page_title="Aplicativo",#Nome da página no chrome
        page_icon="🖥️",#Emoji⚙️🏠📈📊🖥️
        layout="wide" #identifica se é a página inteira
    ) 

st.title('Simulador base de dados')

def convert_df(df):
   return df.to_csv(sep=';').encode('utf-8')

bancodedados = st.file_uploader("Insira o banco de dados no formato Excel (xlsx).")

verificacao_bd = st.button('Executar simulações')
if verificacao_bd:
    try:
        df1 = pd.read_excel(bancodedados)
        X = df1[['ESP_ENSAIO_TR','LARG','C','AL','DESENF','ACAB','BOB','TIPO_CP_D','TIPO_CP_R','TIPO_CP_Y','REV_GA','REV_GI']]
        if ((df1.shape[0] == 0) or (df1.shape[1] == 0)):
            st.warning("O banco de dados está vazio.")
        elif((df1.shape[0] != 0) or (df1.shape[1] != 0)):
            st.success('O banco de dados não está vazio.', icon="✅")
            my_bar = st.progress(0, text="Realizando as predições. Aguarde!")
            for percent_complete in range(100):
                time.sleep(0.001)
                my_bar.progress(percent_complete + 1, text="Realizando as predições. Aguarde!")
            time.sleep(1)
            my_bar.empty()
            with bz2.BZ2File("./modelos/modelo_cat", 'rb') as arquivo:
                modelo_cat = pickle.load(arquivo)
            with bz2.BZ2File("./modelos/modelo_num", 'rb') as arquivo:
                modelo_num = pickle.load(arquivo)
            df1['Chance de rejeição (%)'] = [x[1] for x in modelo_cat.predict_proba(X).tolist()]
            df1['Chance de rejeição (%)'] = df1['Chance de rejeição (%)']*100
            df1['Predições LE'] = modelo_num.predict(X).tolist()
            st.write(df1)
            bot1, bot2, bot3 = st.columns([1.2,1.5,6])
            with bot1:
                st.download_button(label='📥 Download', data=convert_df(df=df1), file_name='Dados e previsões.csv')
            with bot2:
                st.button("❌ Apagar resultados")
    except:
        st.warning("Insira um arquivo válido.")
