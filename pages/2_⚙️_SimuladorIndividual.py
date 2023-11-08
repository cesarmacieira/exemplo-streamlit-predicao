import streamlit as st
import pickle
import bz2
import pandas as pd
import os
from os.path import exists
import xgboost as xgb

st.set_page_config(
        page_title="Aplicativo",#Nome da página no chrome
        page_icon="⚙️",#Emoji⚙️🏠📈📊🖥️
        layout="wide" #identifica se é a página inteira
    ) 

st.title('Simulador individual')

col1, col2, col3 = st.columns(3)
with col1:
    TIPO_CP = st.selectbox("TIPO DE CORPO DE PROVA", ['D','R','Y'])
    if(TIPO_CP == 'D'):
        TIPO_CP_D = 1; TIPO_CP_R = 0; TIPO_CP_Y = 0
    elif(TIPO_CP == 'R'):
        TIPO_CP_D = 0; TIPO_CP_R = 1; TIPO_CP_Y = 0
    else:
        TIPO_CP_D = 0; TIPO_CP_R = 0; TIPO_CP_Y = 1
    REV = st.selectbox("REVESTIMENTO", ['GA','GI'])
    if(REV == 'GA'):
        REV_GA = 1; REV_GI = 0
    else:
        REV_GA = 0; REV_GI = 1
    ESP = st.number_input("ESPESSURA", 0.0, 3.0, step=0.1)
    LARG = st.number_input("LARGURA",700, 8200, step=20)
    C = st.number_input("CARBONO (C)", 3.0, 200.0, step=1.0)
with col2:
    AL = st.number_input("ALUMÍNIO (AL)", 10.0, 90.0, step=10.0)
    DESENF = st.number_input("DESENFORNAMENTO", 1100, 16000, step=10)
    ACAB = st.number_input("ACABAMENTO", 400, 1000, step=10)
    BOB = st.number_input("BOBINAMENTO", 450, 850, step=10)
with col3:
    st.header("Limite de Escoamento")
    bt = st.button('Iniciar simulação')
    if bt:
        with st.spinner('Aguarde...'):
            data = pd.DataFrame({'ESP_ENSAIO_TR':ESP,'LARG':LARG,'C':C,'AL':AL,
                'DESENF':DESENF,'ACAB':ACAB,'BOB':BOB,'TIPO_CP_D':TIPO_CP_D,'TIPO_CP_R':TIPO_CP_R,
                'TIPO_CP_Y':TIPO_CP_Y,'REV_GA':REV_GA,'REV_GI':REV_GI}, index=[0])
            with bz2.BZ2File("./modelos/modelo_cat", 'rb') as arquivo:
                modelo_cat = pickle.load(arquivo)
            with bz2.BZ2File("./modelos/modelo_num", 'rb') as arquivo:
                modelo_num = pickle.load(arquivo)
            prev_cat = modelo_cat.predict_proba(data).tolist()[0][1]
            prev_num = modelo_num.predict(data).tolist()[0]
            st.metric(label = 'Chance de rejeição da bobina', value = f"{round(prev_cat,4)*100}%")
            st.metric(label = 'Estimativa pontual', value = f"{round(prev_num,2)} MPa")
            st.button("❌ Apagar resultados")







