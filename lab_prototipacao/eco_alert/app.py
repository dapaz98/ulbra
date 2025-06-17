import streamlit as st
from views import login_page, register_page, report_page, feed_page
from db import create_tables

st.set_page_config(page_title="Eco Alert", layout="wide")

# Inicializa banco de dados
create_tables()

# Sessão
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

menu = ["Login", "Registrar", "Denúncia", "Feed"]
choice = st.sidebar.selectbox("Navegação", menu)

if choice == "Login":
    login_page()
elif choice == "Registrar":
    register_page()
elif choice == "Denúncia":
    if st.session_state.logged_in:
        report_page()
    else:
        st.warning("Você precisa estar logado.")
elif choice == "Feed":
    feed_page()
