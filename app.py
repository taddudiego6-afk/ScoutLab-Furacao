import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="ScoutLab Hacker", layout="wide")

st.title("🌪️ ScoutLab Furacão - MODO HACKER")
st.write("Invasão na Wikipedia em andamento...")

URL = "https://pt.wikipedia.org/wiki/Club_Athletico_Paranaense"

@st.cache_data(ttl=3600)
def buscar_dados():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        resposta = requests.get(URL, headers=headers)
        
        # O Pandas varre todo o código fonte e pega todas as tabelas
        tabelas = pd.read_html(resposta.text)
        
        # TÁTICA FORÇA BRUTA: Pega a tabela com MAIS LINHAS na página.
        # O elenco ou histórico de jogos sempre são as maiores listas!
        maior_tabela = max(tabelas, key=len)
        
        return maior_tabela
    except Exception as e:
        return f"Erro ao hackear os dados: {e}"

df_live = buscar_dados()

if isinstance(df_live, str):
    st.error(df_live)
else:
    st.success("✅ Firewall quebrado! Maior tabela extraída com sucesso.")
    
    st.subheader("📋 Dados Capturados (Direto da Wikipedia)")
    
    # Mostramos a tabela bruta para você ver o que o robô pescou
    st.dataframe(df_live, use_container_width=True)
    
    st.divider()
    st.write(f"**Linhas capturadas:** {len(df_live)}")
