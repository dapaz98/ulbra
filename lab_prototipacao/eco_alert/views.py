import streamlit as st
import datetime
from db import register_user, check_user, save_report, get_reports
from utils import get_coordinates, save_file
from ia_model import classify_report
import pandas as pd

def login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if check_user(email, password):
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success("Login realizado!")
        else:
            st.error("Credenciais inválidas.")

def register_page():
    st.title("Registrar Conta")
    name = st.text_input("Nome")
    email = st.text_input("Email")
    password = st.text_input("Senha", type="password")
    confirm = st.text_input("Confirmar Senha", type="password")
    if st.button("Registrar"):
        if password == confirm:
            register_user(name, email, password)
            st.success("Registrado com sucesso.")
        else:
            st.error("Senhas não coincidem.")

def report_page():
    st.title("Nova Denúncia Ambiental")
    descricao = st.text_area("Descrição")
    local = st.text_input("Endereço da Ocorrência")
    arquivo = st.file_uploader("Anexe uma Imagem ou Vídeo", type=["png", "jpg", "jpeg", "mp4"])

    if st.button("Enviar"):
        lat, lon = get_coordinates(local)
        categoria, risco = classify_report(descricao)

        file_path = save_file(arquivo)

        save_report(
            email=st.session_state.user_email,
            descricao=descricao,
            tipo=categoria,
            risco=risco,
            data=str(datetime.date.today()),
            local=local,
            latitude=lat,
            longitude=lon,
            arquivo=file_path
        )
        st.success(f"Denúncia registrada como {categoria} com risco {risco}.")

def feed_page():
    st.title("Denúncias Registradas")
    dados = get_reports()
    if dados.empty:
        st.warning("Nenhuma denúncia registrada.")
        return

    filtro = st.selectbox("Filtrar por tipo", ["Todos"] + sorted(dados["tipo"].unique()))
    if filtro != "Todos":
        dados = dados[dados["tipo"] == filtro]

    st.map(dados[["latitude", "longitude"]])

    st.dataframe(dados[["descricao", "tipo", "risco", "data", "local"]])
