import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="ScoutLab Real-Time", layout="wide")

st.title("🌪️ ScoutLab Furacão - MODO HACKER (Live)")
st.write("Buscando dados estatísticos em tempo real no FBref...")

# Link da tabela de estatísticas do Athletico no FBref (Brasileirão 2025/26)
URL = "https://fbref.com/pt/equipes/2091c36b/Athletico-Paranaense-Estatisticas"

@st.cache_data(ttl=3600) # O robô "descansa" por 1 hora antes de buscar de novo
def buscar_dados():
    try:
        # O Pandas tenta ler todas as tabelas da página
        tabelas = pd.read_html(URL, flavor='lxml')
        # A primeira tabela (índice 0) costuma ser a de estatísticas padrão
        df = tabelas[0]
        
        # Limpeza básica (o FBref usa níveis múltiplos de colunas)
        df.columns = df.columns.droplevel(0) 
        return df
    except Exception as e:
        return f"Erro ao hackear os dados: {e}"

df_live = buscar_dados()

if isinstance(df_live, str):
    st.error(df_live)
else:
    # Filtro de jogadores (removendo a linha de 'Total do Plantel')
    df_live = df_live[df_live['Jogador'] != 'Total do Plantel']
    
    st.subheader("📊 Estatísticas Atualizadas (via Web Scraping)")
    st.dataframe(df_live, use_container_width=True)

    # Gráfico de Gols ao Vivo
    st.divider()
    st.subheader("⚽ Gols na Temporada")
    # Convertendo gols para número (às vezes vem como texto no site)
    df_live['Gols'] = pd.to_numeric(df_live['Gols'], errors='coerce').fillna(0)
    st.bar_chart(df_live.set_index("Jogador")["Gols"])
