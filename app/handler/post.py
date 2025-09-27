import streamlit as st
import time

def handle_post_ui(user, comment_manager):
    st.markdown(f"**Logado como:** {user['name']} (`{user['email']}`)")

    if st.button("Sair"):
        st.session_state["user"] = None
        st.session_state["edit_id"] = None
        st.rerun()

    st.subheader("Escreva um comentário")
    with st.form("comment_form"):
        comment_text = st.text_area("Digite seu comentário...", key="new_comment_text")
        submit_comment = st.form_submit_button("Publicar")

        if submit_comment and comment_text:
            msg = comment_manager.publish_comment(user, comment_text)
            
            if "tóxico" in msg.lower() or "bloqueado" in msg.lower():
                st.error(msg)
            else:
                st.success(msg)
                
            time.sleep(0.5)
            st.rerun()