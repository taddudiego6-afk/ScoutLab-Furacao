import streamlit as st
import pandas as pd

# Configuração da página para ficar mais larga
st.set_page_config(layout="wide", page_title="ScoutLab Furacão")

# Título do seu App
st.title("🌪️ Laboratório Tático - Athletico Paranaense")
st.markdown("Bem-vindo ao banco de dados estatístico do Furacão.")

# Carregando os dados que você limpou
df = pd.read_csv('dados_furacao.csv')

# Criando um filtro de posição
posicoes = df['Posicao'].unique()
posicao_selecionada = st.selectbox("Filtre por Posição:", ["Todos"] + list(posicoes))

# Aplicando o filtro
if posicao_selecionada != "Todos":
    df_filtrado = df[df['Posicao'] == posicao_selecionada]
else:
    df_filtrado = df

# Mostrando a tabela na tela
st.write(f"Mostrando dados para: **{posicao_selecionada}**")
st.dataframe(df_filtrado)