import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="ScoutLab Hacker", layout="wide")

st.title("🌪️ ScoutLab Furacão - MODO HACKER")
st.write("Buscando o elenco atualizado em tempo real na Wikipedia...")

# Novo Alvo: Wikipedia (Não bloqueia robôs!)
URL = "https://pt.wikipedia.org/wiki/Club_Athletico_Paranaense"

@st.cache_data(ttl=3600)
def buscar_dados():
    try:
        # O Pandas consegue ler a Wikipedia facilmente
        tabelas = pd.read_html(URL)
        
        # A Wikipedia tem várias tabelas na página. 
        # Vamos procurar a que tem a coluna "Nome" e "Pos." (Posição)
        for tabela in tabelas:
            if 'Nome' in tabela.columns and 'Pos.' in tabela.columns:
                # Limpando colunas inúteis se existirem
                tabela_limpa = tabela[['N.º', 'Pos.', 'Nome', 'Nascimento']]
                return tabela_limpa
                
        return "Tabela de elenco não encontrada na página."
    except Exception as e:
        return f"Erro ao hackear os dados: {e}"

df_live = buscar_dados()

if isinstance(df_live, str):
    st.error(df_live)
else:
    st.success("✅ Acesso concedido! Dados extraídos da Wikipedia com sucesso.")
    
    st.subheader("📋 Elenco Profissional (Tempo Real)")
    # Mostra a tabela bonitona
    st.dataframe(df_live, use_container_width=True)
    
    # Pequeno resumo dos dados hackeados
    st.divider()
    st.write(f"**Total de jogadores encontrados:** {len(df_live)}")
