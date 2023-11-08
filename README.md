# Execução

## Tutorial

* O arquivo "streamlit_parte1.py" contém algumas funções nativas do streamlit.

Detalhes em https://streamlit.io/

* O arquivo "streamlit_parte2.py" é composto pelas funções do arquivo anterior, entretanto com a atualização do uso da função sidebar para organizar em menus.

## Projeto de predição
* O arquivo "Contrução de modelos.ipynb" apresenta a forma da construção dos modelos XGBoost para os limites de escoamento das bobinas para os cenários em que temos problemas de classificação e regressão.
* Os resultados são dois arquivos salvos com o uso da biblioteca bz2 e pickle, e um arquivo "X_teste.xlsx".

* No arquivo "Início.py", está a página inicial do aplicativo.
* Na pasta "pages" estão as 3 páginas do aplicativo:
  1. Análise descritiva: com base nos dados que os modelos foram treinados, realiza uma análise descritiva das variáveis numéricas e categóricas.
  2. Simulação individual: nessa página há os parâmetros que compõem os modelos. Ao preencher com os valores, é possível obter os valores preditos de chance de rejeição da bobina, assim como uma estimativa pontual de um produto com tais características.
  3. Simulação com base de dados: deve-se inserir um arquivo no formato do exemplo "X_teste.xlsx", os modelos são aplicados, as predições acrescentadas e há a opção de download em csv dos dados com as respectivas predições.
 
* **Dados fictícios!!!**
