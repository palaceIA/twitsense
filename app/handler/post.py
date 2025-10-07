import streamlit as st
import time

def handle_post_ui(user, comment_manager):
    st.markdown(f"**Logado como:** {user['name']} (`{user['email']}`)")

    if st.button("Sair"):
        st.session_state["user"] = None
        st.session_state["edit_id"] = None
        st.rerun()

    st.subheader("Escreva um comentário")

    col1, col2 = st.columns([20, 20])

    with col1:
        with st.form("comment_form"):
            comment_text = st.text_area(
                "Digite seu comentário...",
                key="new_comment_text",
                height=200
            )

            topic_name = st.text_input("Tópico do seu comentário")

            submit_comment = st.form_submit_button("Publicar")

            if submit_comment and comment_text:
                topic_ids = []
                if topic_name:
                    topic_id = comment_manager.get_topic_id_by_name(topic_name)
                    if not topic_id:
                        topic_id = comment_manager.create_topic(topic_name)
                    topic_ids = [topic_id]

                comment_manager.publish_comment(user, comment_text, topic_ids)
                time.sleep(0.5)
                st.rerun()

    with col2:
        st.subheader("🌏Estatísticas Globais🌏")

        stats = comment_manager.get_global_topic_sentiment_stats()

        if stats:
            topic_names = [s['topic_name'] for s in stats]
            tabs = st.tabs(topic_names)
            
            for tab, s in zip(tabs, stats):
                with tab:
                    st.write(f"**Total de comentários:** {s['total_comments']}")
                    st.write(f"🟢 Positivo: {s['positive_comments']}")
                    st.write(f"🔴 Negativo: {s['negative_comments']}")
                    st.write(f"🟡 Neutro: {s['neutral_comments']}")
                    st.write(f"⚪ Irrelevante: {s['irrelevant_comments']}")
                    
                    st.progress(float(s['positivity_rate']) / 100 if s['positivity_rate'] else 0)
                    
                    st.caption(f"Média de sentimento: {s['avg_sentiment_score']} | Positividade: {s['positivity_rate']}%")
        else:
            st.info("Nenhum dado disponível ainda.")