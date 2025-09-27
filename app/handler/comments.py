import streamlit as st
import time

def get_sentiment_icon_and_color(sentiment: str) -> str:
    sentiment = sentiment.lower()
    
    mapper = {
        "positivo": ("🟢", "Positivo"),
        "negativo": ("🔴", "Negativo"),
        "neutro": ("🟡", "Neutro"),
        "irrelevante": ("⚪", "Irrelevante"),
    }
    
    return mapper.get(sentiment, ("⚫", "Desconhecido")) 

def handle_comments_ui(user, comment_manager):
    if "edit_id" not in st.session_state:
        st.session_state["edit_id"] = None

    st.subheader("Seus comentários")
    
    sentiment_counts = comment_manager.get_sentiment_counts_by_user(user["id"])

    if sentiment_counts:
        st.markdown("### Resumo de Sentimentos")
        cols = st.columns(len(sentiment_counts))
        icon_map = {
            "positivo": "🟢", "negativo": "🔴",
            "neutro": "🟡", "irrelevante": "⚪"
        }
        
        for i, (sentiment, count) in enumerate(sentiment_counts.items()):
            icon = icon_map.get(sentiment, "⚫")
            with cols[i]:
                st.metric(f"{icon} {sentiment.capitalize()}", value=count)
    else:
        st.info("Você ainda não publicou comentários.")
        return

    comments = comment_manager.get_comments_by_user(user["id"])
    comments_sorted = sorted(comments, key=lambda x: x['id'], reverse=True)
    
    st.markdown("---")
    
    for c in comments_sorted:
        icon, sentiment_name = get_sentiment_icon_and_color(c.get('sentiment', 'Desconhecido'))
        header_text = f"{icon} Comentário {c['id']} | Sentimento: **{sentiment_name}** | Publicado em: {c['created_at'].split('T')[0]}"
        with st.expander(header_text):
            st.markdown(f"**Conteúdo:** {c['comment']}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✏️ Editar", key=f"edit_btn_{c['id']}"):
                    st.session_state["edit_id"] = c['id']
                    st.rerun()
            with col2:
                if st.button("🗑️ Excluir", key=f"delete_btn_{c['id']}"):
                    comment_manager.delete_comment(c["id"])
                    st.success(f"Comentário {c['id']} excluído. Recarregando...")
                    time.sleep(0.5)
                    st.rerun()

            if st.session_state["edit_id"] == c['id']:
                st.markdown("---")
                with st.form(key=f"edit_form_{c['id']}"):
                    new_text = st.text_area("Edite seu comentário", value=c["comment"], key=f"text_area_{c['id']}")
                    
                    col_save, col_cancel = st.columns(2)
                    with col_save:
                        save_comment = st.form_submit_button("💾 Salvar Edição")
                    with col_cancel:
                        cancel_edit = st.form_submit_button("❌ Cancelar")

                    if save_comment:
                        msg = comment_manager.update_comment(c["id"], new_text)
                        st.success(msg)
                        st.session_state["edit_id"] = None
                        time.sleep(0.5)
                        st.rerun()
                    
                    if cancel_edit:
                        st.session_state["edit_id"] = None
                        st.rerun()