import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="ScoutLab - Athletico", layout="wide")

st.title("🌪️ Laboratório Tático - Athletico Paranaense")
st.markdown("Bem-vindo ao banco de dados estatístico do Furacão.")

# Carregar os dados
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

---

# Seção de Gráficos
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Quem é o Garçom? (Assistências)")
    # Gráfico de barras simples do Streamlit
    st.bar_chart(df.set_index("Nome")["Assistencias"])

with col2:
    st.subheader("⚽ Gols por Jogador")
    st.bar_chart(df.set_index("Nome")["Gols"])
