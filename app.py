import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="ScoutLab Hacker", layout="wide")

st.title("🌪️ ScoutLab Furacão - MODO HACKER")
st.write("Buscando o elenco atualizado em tempo real na Wikipedia...")

URL = "https://pt.wikipedia.org/wiki/Club_Athletico_Paranaense"

@st.cache_data(ttl=3600)
def buscar_dados():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        resposta = requests.get(URL, headers=headers)
        tabelas = pd.read_html(resposta.text)
        
        # A nova tática: varrer todas as tabelas e juntar as que parecem ser de elenco
        tabelas_elenco = []
        for tabela in tabelas:
            # Transformamos todos os nomes de colunas em minúsculas para não ter erro
            colunas_minusculas = [str(c).lower() for c in tabela.columns]
            
            # Se a tabela tiver a palavra 'nome' ou 'jogador', é a que queremos!
            if 'nome' in colunas_minusculas or 'jogador' in colunas_minusculas:
                tabelas_elenco.append(tabela)
        
        if len(tabelas_elenco) > 0:
            # Junta todas as partes da tabela (caso a Wikipedia separe goleiros de atacantes)
            df_final = pd.concat(tabelas_elenco, ignore_index=True)
            return df_final
            
        return "Tabela não encontrada. O layout mudou drasticamente."
    except Exception as e:
        return f"Erro ao hackear os dados: {e}"

df_live = buscar_dados()

if isinstance(df_live, str):
    st.error(df_live)
else:
    st.success("✅ Acesso concedido! O Robô varreu a página e encontrou o elenco.")
    
    st.subheader("📋 Elenco Profissional (Tempo Real)")
    
    # Exibe a tabela bruta que o robô conseguiu extrair
    st.dataframe(df_live, use_container_width=True)
    
    st.divider()
    st.write("*(Dados extraídos diretamente da página do Athletico na Wikipedia)*")
