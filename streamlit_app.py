import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sidebar (Menu Lateral)
page = st.sidebar.selectbox("Escolha a Página", ["Visão Geral", "Filtros e Dados"])

def show_overview():
    
    # Visão Geral do Projeto
    st.header("Visão Geral do Projeto")
    st.write("Bem-vindo ao projeto de Visualização de dados de acidentes registrados pela Polícia Rodoviária Federal! "
             "Este projeto gira em torno da análise e apresentação dos dados coletados. O conjunto de dados contém várias colunas fornecendo insights "
             "sobre os produtos e informações relativas aos acidentes, incluindo data, dia da semana, estado, município e causa.")
    
    # Como Funciona
    st.header("Como Funciona")
    st.write("O projeto utiliza um conjunto de dados com informações sobre os acidentes. Aqui está uma breve visão "
             "geral dos principais componentes:")
    
    # Objetivo do Projeto
    st.header("Objetivo do Projeto")
    st.write("O principal objetivo deste projeto é obter insights pela análise dos dados e gráficos criados. Isso inclui entender "
             "o que os dados estão nos dizendo, identificar e explorar padrões.")
    
    # Como Utilizar
    st.header("Como Utilizar")
    st.write("Para explorar o projeto, você pode navegar por diferentes seções usando a barra lateral. As principais seções incluem:")
      
    st.header("Conclusão")
    st.write("Sinta-se à vontade para analisar o conjunto de dados, obter insights e tirar conclusões significativas a partir "
               "dos dados apresentados. Para análises específicas ou dúvidas, novos recursos podem ser incorporados com base nos "
               "objetivos do seu projeto.")
  
    st.write("Aproveite a exploração do projeto visualização dos dados da PRF!")

def show_filters_data():
    st.header("Filtros e Dados")
    df2023 = pd.read_csv('datatran2023.csv', encoding='latin-1', delimiter=';')

    df['dia_semana'] = df['dia_semana'].dt.day_name()
    dia_semana = st.sidebar.selectbox('Selecione o dia', options=df['dia_semana'].unique())
    early_access = st.sidebar.checkbox('Apenas Early Access')
    recommendation = st.sidebar.checkbox('Apenas Recomendados')

    filtered_df = df[df['dia_semana'] == dia_semana]
    if early_access:
        filtered_df = filtered_df[filtered_df['is_early_access_review'] == True]
    if recommendation:
        filtered_df = filtered_df[filtered_df['recommendation'] == "Recommended"]

    municipio = st.sidebar.selectbox('Selecione um Município', options=df['title'].unique())
    municipio_df = filtered_df[filtered_df['title'] == municipio]

    st.write(municipio_df)


    st.header('Gráficos')

    # Média de horas de jogo de cada jogo
    avg_hours = df.groupby('title')['hour_acident'].mean()
    fig, ax = plt.subplots(figsize=(10,4))
    ax.bar(avg_hours.index, avg_hours.values)
    plt.xticks(rotation=90)
    plt.title('Média de Acidentes por Mês')
    plt.xlabel('Acidentes')
    plt.ylabel('Média de Acidentes por Mês')
    st.pyplot(fig)

    # Quantidade de funny
    funny_counts = df.groupby('title')['funny'].sum()
    fig, ax = plt.subplots(figsize=(10,4))
    ax.bar(funny_counts.index, funny_counts.values)
    plt.xticks(rotation=90)
    plt.title('Quantidade de Acidentes por mês')
    plt.xlabel('Acidentes')
    plt.ylabel('Meses')
    st.pyplot(fig)

    # Quantidade de helpful por jogo
    helpful_counts = df.groupby('title')['helpful'].sum()
    fig, ax = plt.subplots(figsize=(10,4))
    ax.bar(helpful_counts.index, helpful_counts.values)
    plt.xticks(rotation=90)
    plt.title('Quantidade de Acidentes por Ano')
    plt.xlabel('Acidentes')
    plt.ylabel('Quantidade de acidentes por Ano')
    st.pyplot(fig)

# Página de Visão Geral
if page == "Visão Geral":
    show_overview()
# Página de Filtros e Dados
elif page == "Filtros e Dados":
    show_filters_data()
