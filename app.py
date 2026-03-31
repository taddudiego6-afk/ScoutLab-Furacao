import streamlit as st
import pandas as pd
import cloudscraper

st.set_page_config(page_title="ScoutLab - HACKER SUPREMO", layout="wide")

st.title("🌪️ ScoutLab Furacão - TÁTICA KAMIKAZE")
st.write("Tentando driblar a segurança máxima do FBref com Cloudscraper...")

# O Alvo: FBref
URL = "https://fbref.com/pt/equipes/2091c36b/Athletico-Paranaense-Estatisticas"

@st.cache_data(ttl=3600)
def buscar_dados_brutos():
    try:
        # 🏴‍☠️ AQUI ENTRA O HACKER: Usando o Cloudscraper no lugar do requests padrão
        scraper = cloudscraper.create_scraper(browser={
            'browser': 'chrome',
            'platform': 'windows',
            'desktop': True
        })
        
        # O Scraper tenta resolver os "desafios" matemáticos invisíveis do site
        resposta = scraper.get(URL)
        
        # Se a resposta for 200, significa que o segurança abriu a porta!
        if resposta.status_code == 200:
            tabelas = pd.read_html(resposta.text, flavor='lxml')
            df = tabelas[0]
            df.columns = df.columns.droplevel(0) # Limpa os títulos duplos do FBref
            return df
        else:
            return f"O juiz deu cartão vermelho! Acesso negado. Status: {resposta.status_code}"
            
    except Exception as e:
        return f"Falha na Matrix ao tentar invadir: {e}"

df_live = buscar_dados_brutos()

if isinstance(df_live, str):
    st.error("🚨 Invasão Falhou!")
    st.error(df_live)
    st.info("O sistema de defesa deles detectou que estamos em um servidor da nuvem (Streamlit Cloud). A zaga é de Copa do Mundo.")
else:
    st.success("✅ GOLAÇO! Driblamos a segurança e entramos no banco de dados!")
    
    # Limpeza para ficar só com os jogadores
    df_live = df_live[df_live['Jogador'].notna()]
    df_live = df_live[df_live['Jogador'] != 'Total do Plantel']
    
    st.subheader("📊 Estatísticas Oficiais do FBref (Em Tempo Real)")
    st.dataframe(df_live, use_container_width=True)
    
    st.divider()
    st.subheader("⚽ Artilheiros da Temporada")
    # Converte para número e arruma o gráfico
    df_live['Gols'] = pd.to_numeric(df_live['Gols'], errors='coerce').fillna(0)
    gols_chart = df_live[df_live['Gols'] > 0].set_index("Jogador")["Gols"].sort_values()
    
    if not gols_chart.empty:
        st.bar_chart(gols_chart, horizontal=True)
