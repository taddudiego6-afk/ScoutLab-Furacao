import streamlit as st
import pandas as pd
import requests

# Configuração da página
st.set_page_config(page_title="ScoutLab Hacker", layout="wide")

st.title("🌪️ ScoutLab Furacão - MODO HACKER")
st.write("Buscando o elenco atualizado em tempo real na Wikipedia...")

URL = "https://pt.wikipedia.org/wiki/Club_Athletico_Paranaense"

@st.cache_data(ttl=3600)
def buscar_dados():
    try:
        # 1. Colocamos o disfarce de navegador comum
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        # 2. Entramos no site com o disfarce
        resposta = requests.get(URL, headers=headers)
        
        # 3. O Pandas lê as tabelas do código-fonte que baixamos
        tabelas = pd.read_html(resposta.text)
        
        # 4. Procuramos a tabela certa do elenco
        for tabela in tabelas:
            if 'Nome' in tabela.columns and 'Pos.' in tabela.columns:
                # Retorna só as colunas importantes
                return tabela[['N.º', 'Pos.', 'Nome', 'Nascimento']]
                
        return "Tabela não encontrada. O layout da Wikipedia pode ter mudado."
    except Exception as e:
        return f"Erro ao hackear os dados: {e}"

df_live = buscar_dados()

if isinstance(df_live, str):
    st.error(df_live)
else:
    st.success("✅ Acesso concedido! Zaga driblada e dados extraídos com sucesso.")
    
    st.subheader("📋 Elenco Profissional (Tempo Real)")
    # Remove as linhas de subtítulos que a Wikipedia às vezes coloca
    df_live = df_live.dropna(subset=['N.º'])
    
    st.dataframe(df_live, use_container_width=True)
    
    st.divider()
    st.write(f"**Jogadores listados:** {len(df_live)}")
