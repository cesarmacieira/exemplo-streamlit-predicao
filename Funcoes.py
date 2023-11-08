#Função para realizar a análise descritiva de uma variável categórica
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

#Função para realizar a análise descritiva de uma variável numérica
def DescritivaNum(df,cols): #(df = dados, cols = variável(is) categórica(s))
    result = df[cols].describe().transpose()             
    result = result.reset_index()
    result.columns = ['Variável','Freq. Absoluta','Média','Desvio Padrão','Mínimo','Q1','Q2 (Mediana)','Q3','Máximo']
    return result

#Função para realizar a análise descritiva de uma variável numérica por uma variável categórica
def Descritiva1Num1Cat(dados,var_num,var_cat):
    dados = dados.dropna(subset=[var_num])
    tabela = dados.groupby(var_cat)[var_num].describe().round(2)
    tabela = tabela.reset_index()
    tabela.columns = ['Variável','Freq. Absoluta','Média','Desvio Padrão','Mínimo','Q1','Q2 (Mediana)','Q3','Máximo']
    return tabela

#Função para realizar a análise descritiva de uma ou mais variável(is) numérica(s) por uma variável categórica
def DescritivaVarNum1Cat(dados, var_nums, var_cat):
    tabelas = []
    for var_num in var_nums:
        dados_filtrados = dados.dropna(subset=[var_num])
        tabela = dados_filtrados.groupby(var_cat)[var_num].describe().round(2)
        tabela = tabela.reset_index()
        tabela.rename(columns={var_num: 'Variável'}, inplace=True)
        tabela.insert(0, 'Variavel', var_num)
        tabela['Churn'] = tabela[var_cat]
        tabelas.append(tabela)
    resultado_final = pd.concat(tabelas, ignore_index=True)
    return resultado_final

#Função para realizar a análise descritiva de uma variável categórica por uma variável categórica e aplicar o teste Qui-Quadrado
def Comparações1VarCat1VarCat(dataset, variavel1, variavel2, LinhaColuna="Linha"):
    dados = dataset.dropna(subset=[variavel1,variavel2])
    df = pd.DataFrame(dados)
    niveis_variavel1 = df[variavel1].unique()
    niveis_variavel2 = df[variavel2].unique()
    tabela_contingencia_parts = []
    for nivel1 in niveis_variavel1:
        for nivel2 in niveis_variavel2:
            contagem = len(df[(df[variavel1] == nivel1) & (df[variavel2] == nivel2)])
            tabela_contingencia_parts.append({variavel1: nivel1, variavel2: nivel2, 'Freq. Absoluta': contagem})
    tabela_contingencia = pd.concat([pd.DataFrame(part, index=[0]) for part in tabela_contingencia_parts], ignore_index=True)
    if LinhaColuna == "Coluna":
        for nivel2 in niveis_variavel2:
            total_coluna = tabela_contingencia[tabela_contingencia[variavel2] == nivel2]['Freq. Absoluta'].sum()
            tabela_contingencia.loc[tabela_contingencia[variavel2] == nivel2, 'Freq. Relativa'] = (tabela_contingencia[tabela_contingencia[variavel2] == nivel2]['Freq. Absoluta'] / total_coluna)*100
        tabela_contingencia = tabela_contingencia.sort_values(by=variavel2)
    elif LinhaColuna == "Linha":
        for nivel1 in niveis_variavel1:
            total_linha = tabela_contingencia[tabela_contingencia[variavel1] == nivel1]['Freq. Absoluta'].sum()
            tabela_contingencia.loc[tabela_contingencia[variavel1] == nivel1, 'Freq. Relativa'] = (tabela_contingencia[tabela_contingencia[variavel1] == nivel1]['Freq. Absoluta'] / total_linha)*100
            tabela_contingencia = tabela_contingencia.sort_values(by=[variavel1,variavel2])
    observed = pd.crosstab(df[variavel1], df[variavel2])
    chi2, p, _, _ = chi2_contingency(observed)
    tabela_contingencia['Qui-Quadrado'] = p
    return tabela_contingencia
    
#Função para realizar a análise descritiva de uma ou mais variável(is) numérica(s) por uma variável categórica, verificar normalidade e aplicar teste de hipóteses
def Comparações1VarNum1VarCat(dados, var_nums, var_cat, DepIndep="Independente"):
    tabelas = []
    for var_num in var_nums:
        dados_filtrados = dados.dropna(subset=[var_num])
        tabela = dados_filtrados.groupby(var_cat)[var_num].describe().round(2)
        tabela = tabela.reset_index()
        tabela.rename(columns={var_num: 'Variável'}, inplace=True)
        tabela.insert(0, 'Variavel', var_num)
        tabela['Churn'] = tabela[var_cat]
        n = len(dados_filtrados)
        if n <= 5000:
            _, p_value_norm = stats.shapiro(dados_filtrados[var_num])
            normalidade = round(p_value_norm, 5)
            tabela['Normalidade (SW)'] = normalidade
        else:
            _, p_value_norm = stats.kstest(dados_filtrados[var_num], 'norm')
            normalidade = round(p_value_norm, 5)
            tabela['Normalidade (KS)'] = normalidade
        num_niveis_var_cat = len(dados_filtrados[var_cat].unique())
        if DepIndep == "Independente":
            if p_value_norm > 0.05:
                if num_niveis_var_cat == 2:
                    _, p_value_teste = stats.ttest_ind(dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[0]][var_num],
                                                       dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[1]][var_num])
                    tabela['Teste T'] = round(p_value_teste, 3)
                else:
                    _, p_value_teste = stats.f_oneway(*[dados_filtrados[dados_filtrados[var_cat] == nivel][var_num] for nivel in dados_filtrados[var_cat].unique()])
                    tabela['ANOVA'] = round(p_value_teste, 3)
            else:
                if num_niveis_var_cat == 2:
                    _, p_value_teste = stats.mannwhitneyu(dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[0]][var_num],
                                                          dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[1]][var_num])
                    tabela['Mann-Whitney'] = round(p_value_teste, 3)
                else:
                    _, p_value_teste = stats.kruskal(*[dados_filtrados[dados_filtrados[var_cat] == nivel][var_num] for nivel in dados_filtrados[var_cat].unique()])
                    tabela['Kruskal-Wallis'] = round(p_value_teste, 3)
        else:
            if p_value_norm > 0.05:
                if num_niveis_var_cat == 2:
                    _, p_value_teste = stats.ttest_rel(dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[0]][var_num],
                                                       dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[1]][var_num])
                    tabela['T Teste Dependente'] = round(p_value_teste, 3)
                else:
                    _, p_value_teste = stats.f_oneway(*[dados_filtrados[dados_filtrados[var_cat] == nivel][var_num] for nivel in dados_filtrados[var_cat].unique()])
                    tabela['ANOVA Dependente'] = round(p_value_teste, 3)
            else:
                if num_niveis_var_cat == 2:
                    _, p_value_teste = stats.wilcoxon(dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[0]][var_num],
                                                      dados_filtrados[dados_filtrados[var_cat] == dados_filtrados[var_cat].unique()[1]][var_num])
                    tabela['Wilcoxon'] = round(p_value_teste, 3)
                else:
                    _, p_value_teste = stats.friedmanchisquare(*[dados_filtrados[dados_filtrados[var_cat] == nivel][var_num] for nivel in dados_filtrados[var_cat].unique()])
                    tabela['Friedman'] = round(p_value_teste, 3)
        tabelas.append(tabela)
    resultado_final = pd.concat(tabelas, ignore_index=True)
    resultado_final.rename(columns={'count': 'Freq. Absoluta', 'mean': 'Média', 'std': 'Desvio Padrão', 'min': 'Mínimo', '25%': 'Q1', '50%': 'Q2 (Mediana)',
                                    '75%': 'Q3','max': 'Máximo'}, inplace=True)
    return resultado_final