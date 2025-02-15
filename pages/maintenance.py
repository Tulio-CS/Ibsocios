import streamlit as st
import pandas as pd

st.set_page_config(page_title="DiselMais - Gestão de Frotas", layout="wide")

# Sidebar Title
st.sidebar.title("DiselMais - Gestão de Frotas")
st.sidebar.markdown("---")

# Navigation Links
st.sidebar.page_link("pages/vehicles.py", label="Meus Carros")
st.sidebar.page_link("pages/maintenance.py", label="Manutenções")
st.sidebar.page_link("pages/reports.py", label="Relatórios")

st.sidebar.markdown("---")
st.sidebar.info("Versão 1.0 | Desenvolvido por IbSocios")
    
st.subheader("Receitas Mensais")
data = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai"],
    "Receita (R$)": [75000, 60000, 85000, 70000, 90000]
}
df = pd.DataFrame(data)
st.bar_chart(df.set_index("Mês"))