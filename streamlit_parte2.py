import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title('Streamlit')
add_selectbox = st.sidebar.selectbox("Seção",("Textos","Elementos de dados","Configurações de colunas",
                                              "Gráficos","Widgets","Elementos de mídia","Elementos de status",
                                              "Colunas","Tabs","Contêiner"))

if add_selectbox == "Textos":
    st.title('Seção: Textos')

    st.write('<b>st.write</b>: escrever argumentos para o aplicativo.', unsafe_allow_html=True)
    st.write('Usiminas')

    st.write('<b>st.title</b>: exibir texto na formatação de título.', unsafe_allow_html=True)
    st.title('Usiminas')

    st.write('<b>st.code</b>: exibir um bloco de código com destaque de sintaxe opcional.', unsafe_allow_html=True)
    st.code('Usiminas')

    st.write('<b>st.text</b>: escrever texto de largura fixa e pré-formatado.', unsafe_allow_html=True)
    st.text('Usiminas')

    st.write('<b>st.header</b>: exibir texto na formatação de cabeçalho.', unsafe_allow_html=True)
    st.header('Usiminas')

    st.write('<b>st.subheader</b>: exibir texto na formatação de subcabeçalho.', unsafe_allow_html=True)
    st.subheader('Usiminas')

    st.write('<b>st.caption</b>: exibir texto em fonte pequena.', unsafe_allow_html=True)
    st.caption('Usiminas')

    st.write('<b>st.latex</b>: exibir expressões matemáticas formatadas como LaTeX.', unsafe_allow_html=True)
    st.latex('Usiminas')

    st.write('<b>st.divider</b>: traçar uma linha horizontal.', unsafe_allow_html=True)
    st.divider()

if add_selectbox == "Elementos de dados":
    st.title('Seção: Elementos de dados')
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.write('<b>st.dataframe</b>: exibe dataframe como uma tabela interativa.', unsafe_allow_html=True)
    st.dataframe(df)

    st.write('<b>st.data_editor</b>: exibe um widget de editor de dados.', unsafe_allow_html=True)
    df = pd.DataFrame([{"command": "st.selectbox", "rating": 4, "is_widget": True}, 
                    {"command": "st.balloons", "rating": 5, "is_widget": False},
                    {"command": "st.time_input", "rating": 3, "is_widget": True},])
    edited_df = st.data_editor(df)

    st.write('<b>st.table</b>: exibe uma tabela estática.', unsafe_allow_html=True)
    df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
    st.table(df)

    st.write('<b>st.metric</b>: exibe uma métrica em fonte grande e em negrito, com um indicador opcional de como a métrica mudou.', unsafe_allow_html=True)
    st.metric(label="Temperature", value="13 °C", delta="1.2 °C")

    st.write('<b>st.json</b>: exibe objeto ou string como uma string JSON.', unsafe_allow_html=True)
    st.json({'foo': 'bar','baz': 'boz','stuff': ['stuff 1','stuff 2','stuff 3','stuff 5']})

if add_selectbox == "Configurações de colunas":
    st.title('Seção: Configurações de colunas')
    st.write('<b>st.columns_config.Column</b>: configurar uma coluna genérica em um dataframe.', unsafe_allow_html=True)
    data_df = pd.DataFrame({"widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"]})
    st.data_editor(data_df,column_config={"widgets": st.column_config.Column("Streamlit Widgets",
            help="Streamlit **widget** commands 🎈", width="medium", required=True)},
            hide_index=True, num_rows="dynamic")

    st.write('<b>st.columns_config.TextColumn</b>: configurar uma coluna de texto.', unsafe_allow_html=True)
    data_df = pd.DataFrame({"widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"]})
    st.data_editor(data_df,column_config={"widgets": st.column_config.TextColumn("Widgets",help="Streamlit **widget** commands 🎈",
            default="st.",max_chars=50,validate="^st\.[a-z_]+$")},hide_index=True)

    st.write('<b>st.columns_config.NumberColumn</b>: configurar uma coluna numérica.', unsafe_allow_html=True)
    data_df = pd.DataFrame({"price": [20, 950, 250, 500]})
    st.data_editor(data_df,column_config={"price": st.column_config.NumberColumn("Price (in USD)",help="The price of the product in USD",
            min_value=0,max_value=1000,step=1,format="$%d")},hide_index=True)

    st.write('<b>st.columns_config.CheckboxColumn</b>: configurar uma coluna de caixa de seleção.', unsafe_allow_html=True)
    data_df = pd.DataFrame({"widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],"favorite": [True, False, False, True]})
    st.data_editor(data_df,column_config={"favorite": st.column_config.CheckboxColumn("Your favorite?",help="Select your **favorite** widgets",
            default=False)},disabled=["widgets"],hide_index=True)

    st.write('<b>st.columns_config.ImageColumn</b>: configurar uma coluna de imagem.', unsafe_allow_html=True)
    data_df = pd.DataFrame({"apps": ["https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png"]})
    st.data_editor(data_df,column_config={"apps": st.column_config.ImageColumn("Preview Image", help="Streamlit app preview screenshots")},
                hide_index=True)

if add_selectbox == "Gráficos":
    st.title('Seção: Gráficos')
    st.write('<b>st.area_chart</b>: gráfico de área.', unsafe_allow_html=True)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)

    st.write('<b>st.bar_chart</b>: gráfico de barras.', unsafe_allow_html=True)
    st.bar_chart(chart_data)

    st.write('<b>st.line_chart</b>: gráfico de linhas.', unsafe_allow_html=True)
    st.line_chart(chart_data)

    st.write('<b>st.scatter_chart</b>: gráfico de dispersão.', unsafe_allow_html=True)
    st.scatter_chart(chart_data)

if add_selectbox == "Widgets":
    st.title('Seção: Widgets')
    st.write('<b>st.button</b>: botão.', unsafe_allow_html=True)
    st.button("Reset", type="primary")
    if st.button('Aperte e terá uma surpresa!'):
        st.write('Enganei o bobo.')

    st.write('<b>st.download_button</b>: botão para realizar o download de algum arquivo.', unsafe_allow_html=True)
    csv = chart_data.to_csv().encode('utf-8')
    st.download_button(label="Download no formato CSV", data=csv, file_name='large_df.csv', mime='text/csv')

    st.write('<b>st.link_button</b>: botão para abrir uma URL especificada.', unsafe_allow_html=True)
    st.link_button("Ir para site da Usiminas", "https://www.usiminas.com/")

    st.write('<b>st.checkbox</b>: caixa de seleção.', unsafe_allow_html=True)
    agree = st.checkbox('Concordo com os termos de uso.')
    if agree:
        st.write('Ótimo!')

    st.write('<b>st.toggle</b>: alternância.', unsafe_allow_html=True)
    on = st.toggle('Botão de ativação')
    if on:
        st.write('Ativado!')

    st.write('<b>st.radio</b>: botão de opção.', unsafe_allow_html=True)
    genre = st.radio("What's your favorite movie genre", [":rainbow[Comédia]", "***Drama***", "Documentário :movie_camera:"],
        captions = ["Sorria.", "Pegue a pipoca.", "Não pare de aprender."])
    if genre == ':rainbow[Comédia]':
        st.write('Você selecionou comédia.')
    else:
        st.write("Você não selecionou comédia.")

    st.write('<b>st.selectbox</b>: seleção de uma opção.', unsafe_allow_html=True)
    option = st.selectbox('Você torce para qual time?', ('Atlético', 'Outro'))

    st.write('<b>st.selectbox</b>: seleção de uma ou mais opções.', unsafe_allow_html=True)
    options = st.multiselect('Qual(is) marca(s) você conhece?', ['AAA', 'BBB', 'CCC', 'DDD'], ['AAA', 'CCC'])
    st.write('Você selecionou:', options)

    st.write('<b>st.slider</b>: seleção de um range.', unsafe_allow_html=True)
    values = st.slider('Selecione a amplitude', 0.0, 100.0, (25.0, 75.0))

if add_selectbox == "Elementos de mídia":
    st.title('Seção: Elementos de mídia')
    st.write('<b>st.image</b>: exibir uma imagem.', unsafe_allow_html=True)
    image = Image.open('Alto-Fornos.jpg')
    st.image(image, caption='Alto fornos Usiminas')

    st.write('<b>st.audio</b>: reproduzir um áudio.', unsafe_allow_html=True)
    audio_file = open('myaudio.ogg', 'rb')
    audio_bytes = audio_file.read()#
    st.audio(audio_bytes, format='audio/ogg')

if add_selectbox == "Elementos de status":
    st.title('Seção: Elementos de status')
    import time
    st.write('<b>st.chat_input</b>: barra de progresso.', unsafe_allow_html=True)
    progress_text = "Em execução, espere terminar."
    executar = st.button("Executar")
    if executar:
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()

    st.write('<b>st.spinner</b>: mensagem temporária até a execução de um código.', unsafe_allow_html=True)
    executar1 = st.button("Executar!") 
    if executar1:
        with st.spinner('Carregando...'):
            time.sleep(4)
        st.success('Concluído!')

    st.write('<b>st.balloons e st.snow</b>: surgimento de balões e neve.', unsafe_allow_html=True)
    balao = st.button("BALÕES!!!")
    if balao:
        st.balloons()
    neve = st.button("NEVE!!!")
    if neve:
        st.snow()
        st.write('Além de organizar por seções, pode-se dividir em colunas a composição das páginas.')

if add_selectbox == "Colunas":
    st.title('Seção: Colunas')
    graf1, graf2 = st.columns(2)
    with graf1:
        st.write('<b>st.area_chart</b>: gráfico de área.', unsafe_allow_html=True)
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        st.area_chart(chart_data)
        st.write('<b>st.bar_chart</b>: gráfico de barras.', unsafe_allow_html=True)
        st.bar_chart(chart_data)
    with graf2:
        st.write('<b>st.line_chart</b>: gráfico de linhas.', unsafe_allow_html=True)
        st.line_chart(chart_data)
        st.write('<b>st.scatter_chart</b>: gráfico de dispersão.', unsafe_allow_html=True)
        st.scatter_chart(chart_data)

if add_selectbox == "Tabs":
    st.title('Seção: Tabs')
    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

if add_selectbox == "Contêiner":
    st.title('Seção: Contêiner')
    with st.container():
        st.write("Serve para inserir elementos fora de ordem.")
        st.bar_chart(np.random.randn(50, 3))
    st.write("Texto fora do contêiner.")