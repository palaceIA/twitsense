class CommentManager:
    def __init__(self, supabase_client, user_manager, model_predict_fn):
        self.supabase = supabase_client
        self.user_manager = user_manager
        self.model_predict_fn = model_predict_fn

    def publish_comment(self, user: dict, comment_text: str, topic_ids: list[int] = None) -> str:
        user_id = user["id"]
        client = self.supabase.conn
        sentiment = self.model_predict_fn(comment_text)

        # Insere o comentário
        res = client.table("comments").insert({
            "user_id": user_id,
            "comment": comment_text,
            "sentiment": sentiment
        }).execute()

        if not res.data:
            return "Erro ao publicar comentário."

        comment_id = res.data[0]["id"]

        if comment_id and topic_ids:
            topic_relations = [{"comment_id": comment_id, "topic_id": tid} for tid in topic_ids if tid is not None]
            try:
                client.table("comment_topics").insert(topic_relations).execute()
            except Exception as e:
                print("❌ ERRO AO INSERIR EM comment_topics:")
                print(e)
                print("topic_relations:", topic_relations)
                return f"Erro ao vincular tópicos: {e}"
        
        return "Comentário publicado com sucesso!"


    def get_sentiment_counts_by_user(self, user_id: int) -> dict:

        client = self.supabase.conn
        res = client.rpc("get_user_sentiment_counts", {"p_user_id": user_id}).execute()

        if res.data:
            return {item["sentiment"]: item["count"] for item in res.data}
        return {}
    
    def get_comments_by_user(self, user_id: int):
        client = self.supabase.conn
        res = client.table("comments").select("*").eq("user_id", user_id).execute()
        return res.data

    def get_topic_id_by_name(self, topic_name: str) -> int | None:
        client = self.supabase.conn
        res = client.table("topics").select("id").eq("name", topic_name).execute()

        if res.data and len(res.data) > 0:
            return res.data[0]["id"]
        return None
    
    def create_topic(self, topic_name: str) -> int | None:
        client = self.supabase.conn
        res = client.table("topics").insert({"name": topic_name}).execute()
        if res.data and len(res.data) > 0:
            return res.data[0]["id"]
        existing = client.table("topics").select("id").eq("name", topic_name).execute()
        if existing.data:
            return existing.data[0]["id"]
        return None
        
    def get_global_topic_sentiment_stats(self):
        client = self.supabase.conn
        res = client.table("global_topic_sentiment_stats").select("*").execute()
        if res.data:
            return res.data
        return []

    def update_comment(self, comment_id: int, new_text: str, topic_ids: list[int] = None) -> str:
        client = self.supabase.conn
        new_sentiment = self.model_predict_fn(new_text)

        client.table("comments").update({
            "comment": new_text,
            "sentiment": new_sentiment,
            "updated_at": "NOW()"
        }).eq("id", comment_id).execute()

        if topic_ids is not None:
            client.table("comment_topics").delete().eq("comment_id", comment_id).execute()
            topic_relations = [{"comment_id": comment_id, "topic_id": tid} for tid in topic_ids]
            client.table("comment_topics").insert(topic_relations).execute()

        return "Comentário atualizado com sucesso."

    def delete_comment(self, comment_id: int) -> str:
        client = self.supabase.conn
        client.table("comments").delete().eq("id", comment_id).execute()
        return "Comentário excluído."
