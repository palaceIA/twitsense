class CommentManager:
    def __init__(self, supabase_client, user_manager, model_predict_fn):
        self.supabase = supabase_client
        self.user_manager = user_manager
        self.model_predict_fn = model_predict_fn

    def publish_comment(self, user: dict, comment_text: str) -> str:
        user_id = user['id']
        client = self.supabase.conn
        sentiment = self.model_predict_fn(comment_text) 
        client.table("comments").insert({
                "user_id": user_id,
                "comment": comment_text,
                "sentiment": sentiment
            }).execute()
        
        return "Comentário publicado com sucesso!"
    
    def get_sentiment_counts_by_user(self, user_id: int) -> dict:
        client = self.supabase.conn
        res = client.rpc(
            "get_user_sentiment_counts", 
            {"p_user_id": user_id} 
        ).execute()
        
        if res.data:
            counts = {item['sentiment']: item['count'] for item in res.data}
            return counts
        
        return {}

    def get_comments_by_user(self, user_id: int):
        client = self.supabase.conn
        res = client.table("comments").select("*").eq("user_id", user_id).execute()
        return res.data

    def update_comment(self, comment_id: int, new_text: str):
        client = self.supabase.conn
        
        new_sentiment = self.model_predict_fn(new_text)
        client.table("comments").update({
            "comment": new_text,
            "sentiment": new_sentiment,
            "updated_at": "NOW()" 
            }).eq("id", comment_id).execute()
        return "Comentário atualizado com sucesso."

    def delete_comment(self, comment_id: int):
        client = self.supabase.conn
        client.table("comments").delete().eq("id", comment_id).execute()
        return "Comentário excluído."