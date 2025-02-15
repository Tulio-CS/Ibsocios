import streamlit as st
import pandas as pd

def homePage(t):                    
    st.set_page_config(page_title="DiselMais - Gestão de Frotas", layout="wide")

    with open ('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
                        
    # Sidebar Title
    st.sidebar.title("DiselMais - Gestão de Frotas")
    st.sidebar.markdown("---")

    # Navigation Links
    st.sidebar.page_link("pages/vehicles.py", label="Meus Carros")
    st.sidebar.page_link("pages/maintenance.py", label="Manutenções")
    st.sidebar.page_link("pages/reports.py", label="Relatórios")

    st.sidebar.markdown("---")
    st.sidebar.info("Versão 1.0 | Desenvolvido por IbSocios")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="🚛 Frota Total", value=t, delta="+2 este mês")

    with col2:
        st.metric(label="🛠️ Manutenções", value="8", delta="3 pendentes")

    with col3:
        st.metric(label="⛽ Gastos Combustível", value="R$ 45.280", delta="-5% vs. último mês")

    with col4:
        st.metric(label="⚠️ Multas Ativas", value="3", delta="2 em recurso")

    st.markdown("---")

    # Criando as seções de Receita Mensal e Atividades Recentes
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Receitas Mensais")
        st.bar_chart({"Receitas": [75000, 60000, 85000, 70000, 90000, 65000]},width=150,horizontal=True)

    with col2:
        st.subheader("📌 Atividades Recentes")
        st.write("📌 **Novo veículo cadastrado** - Caminhão Mercedes-Benz Atego 2430 (2h atrás)")
        st.write("🔧 **Manutenção agendada** - Troca de óleo - Placa ABC-1234 (4h atrás)")
        st.write("⛽ **Abastecimento registrado** - R$ 450,00 - 100L Diesel S10 (6h atrás)")

    st.markdown("---")

    # Criando widgets extras para alertas e documentos pendentes
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🛠️ Próximas Manutenções")
        st.markdown(
            """
            <div style="background-color:#fff5eb; padding:10px; border-radius:10px;">
                <b style="color:#d9822b;">Troca de Óleo</b> <span style="float:right;">Em 3 dias</span><br>
                Placa: <b>ABC-1234</b>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.subheader("📦 Alertas de Estoque")
        st.markdown(
            """
            <div style="background-color:#ffecec; padding:10px; border-radius:10px;">
                <b style="color:#d93030;">Filtro de Óleo</b> <span style="float:right;">Estoque Baixo</span><br>
                Restam <b>2 unidades</b>
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.subheader("📄 Documentos Pendentes")
        st.markdown(
            """
            <div style="background-color:#e3f2fd; padding:10px; border-radius:10px;">
                <b style="color:#1565c0;">Renovação ANTT</b> <span style="float:right;">Vence em 15 dias</span><br>
                2 veículos
            </div>
            """, unsafe_allow_html=True
        )



if __name__ == '__main__':
    home()