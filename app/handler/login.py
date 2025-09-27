import streamlit as st
import time

def handle_login_ui(user_manager):
    if st.session_state["user"]:
        return 

    st.subheader("Identifique-se para postar")
    with st.form("user_form"):
        name = st.text_input("Nome")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            if name and email:
                user = user_manager.get_or_create_user(name, email)
                
                if user is None:
                    st.error("Erro ao encontrar ou criar usuário.")
                else:
                    st.session_state["user"] = user
                    st.success(f"Bem-vindo(a), {user['name']}!")
                    time.sleep(0.5)
                    st.rerun()
            else:
                st.warning("Preencha todos os campos.")
    st.stop()
