
class UserManager:
    def __init__(self, supabase_client):

        self.supabase = supabase_client

    def get_or_create_user(self, name: str, email: str) -> dict | None:
        client = self.supabase.conn

        res = client.table("users").select("*").eq("email", email).limit(1).execute()
        if res.data:
            return res.data[0]

        new_user_res = client.table("users").insert({"name": name, "email": email}).execute()
        if new_user_res.data:
                return new_user_res.data[0]
        return None
