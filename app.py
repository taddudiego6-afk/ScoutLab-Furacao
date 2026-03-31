import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="ScoutLab - Athletico", layout="wide")

st.title("🌪️ Laboratório Tático - Athletico Paranaense")
st.markdown("Bem-vindo ao banco de dados estatístico do Furacão.")

# Carregar os dados (Seu arquivo CSV)
df = pd.read_csv("dados_furacao.csv")

# Filtro lateral
st.sidebar.header("Filtros")
posicao = st.sidebar.selectbox("Filtre por Posição:", ["Todos"] + list(df['Posicao'].unique()))

if posicao != "Todos":
    df_filtrado = df[df['Posicao'] == posicao]
else:
    df_filtrado = df

# Exibir Tabela
st.subheader(f"Mostrando dados para: {posicao}")
st.dataframe(df_filtrado, use_container_width=True)

# SEÇÃO DE GRÁFICOS (MODERNA E HORIZONTAL)
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Garçons (Assistências)")
    # Organizamos do menor para o maior para o melhor ficar no topo do gráfico horizontal
    assistencias = df[['Nome', 'Assistencias']].set_index('Nome').sort_values('Assistencias', ascending=True)
    # Filtramos para mostrar apenas quem tem pelo menos 1 assistência (limpa o gráfico)
    assistencias = assistencias[assistencias['Assistencias'] > 0]
    st.bar_chart(assistencias, horizontal=True)

with col2:
    st.subheader("⚽ Artilharia (Gols)")
    gols = df[['Nome', 'Gols']].set_index('Nome').sort_values('Gols', ascending=True)
    # Filtramos para mostrar apenas quem já marcou gol
    gols = gols[gols['Gols'] > 0]
    st.bar_chart(gols, horizontal=True)
