import streamlit as st

from service.supabase.comment import CommentManager
from service.supabase.user import UserManager
from service.supabase.client import supabase 
from service.predict.input import predictor

from handler.comments import handle_comments_ui
from handler.login import handle_login_ui
from handler.post import handle_post_ui


user_manager = UserManager(supabase)

comment_manager = CommentManager(
    supabase, 
    user_manager, 
    lambda text: predictor.predict([text])
)

if __name__ == "__main__":
    st.set_page_config(page_title="Mini Twitter", layout="centered")
    st.title("TwitSense🐦")

    if "user" not in st.session_state:
        st.session_state["user"] = None
    if "edit_id" not in st.session_state:
        st.session_state["edit_id"] = None

    handle_login_ui(user_manager)

    user = st.session_state["user"]

    handle_post_ui(user, comment_manager)

    handle_comments_ui(user, comment_manager)