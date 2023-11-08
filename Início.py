import streamlit as st
from PIL import Image

st.set_page_config(
        page_title="Aplicativo",#Nome da página no chrome
        page_icon="🏭",#Emoji⚙️🏠📈📊🖥️
        layout="wide" #identifica se é a página inteira
    ) 
st.sidebar.image(Image.open('./Arquivos/Logo.png'))

st.title('Predição de Propriedades Mecânicas')
st.markdown('<p>Predição do limite de escoamento das bobinas<br>versão: 1.0.0</p>', unsafe_allow_html=True)
st.markdown('<p>César Macieira</p>', unsafe_allow_html=True)