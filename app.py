import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="ScoutLab Real-Time", layout="wide")

st.title("🌪️ ScoutLab Furacão - MODO HACKER (Live)")
st.write("Buscando dados estatísticos em tempo real no FBref...")

# Link da tabela de estatísticas do Athletico
URL = "https://fbref.com/pt/equipes/2091c36b/Athletico-Paranaense-Estatisticas"

@st.cache_data(ttl=3600)
def buscar_dados():
    try:
        # --- O DISFARCE HACKER ---
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Baixamos a página com o disfarce
        resposta = requests.get(URL, headers=headers)
        
        # O Pandas lê as tabelas dentro da resposta do site
        tabelas = pd.read_html(resposta.text, flavor='lxml')
        
        # Pegamos a primeira tabela e limpamos os títulos duplos
        df = tabelas[0]
        df.columns = df.columns.droplevel(0) 
        return df
    except Exception as e:
        return f"Erro ao hackear os dados: {e}"

df_live = buscar_dados()

if isinstance(df_live, str):
    st.error(df_live)
else:
    # Limpeza para focar nos jogadores reais
    df_live = df_live[df_live['Jogador'] != 'Total do Plantel']
    
    st.subheader("📊 Estatísticas Atualizadas (via Web Scraping)")
    st.dataframe(df_live, use_container_width=True)

    # Gráfico de Gols ao Vivo
    st.divider()
    st.subheader("⚽ Artilharia em Tempo Real")
    df_live['Gols'] = pd.to_numeric(df_live['Gols'], errors='coerce').fillna(0)
    # Filtramos só quem tem gol para o gráfico ficar bonito
    gols_chart = df_live[df_live['Gols'] > 0].set_index("Jogador")["Gols"].sort_values()
    st.bar_chart(gols_chart, horizontal=True)    st.divider()
    st.subheader("⚽ Gols na Temporada")
    # Convertendo gols para número (às vezes vem como texto no site)
    df_live['Gols'] = pd.to_numeric(df_live['Gols'], errors='coerce').fillna(0)
    st.bar_chart(df_live.set_index("Jogador")["Gols"])
