from supabase import (
    create_client , 
    Client
)

from dataclasses import dataclass
from core.settings import configs

@dataclass
class SupabaseConnection : 
    url : str = configs.SUPABASE_URL
    key : str = configs.SUPABASE_KEY


class ClientSupabase:
    def __init__(self, conn: SupabaseConnection):
        if not conn.url or not conn.key:
            raise ValueError("URL ou KEY do Supabase não fornecidos.")
        self._conn = create_client(conn.url, conn.key)

    def verify_conn(self) -> bool:
        try:
            res = self._conn.table("users").select("*").limit(1).execute()
            return res.status_code == 200
        except Exception as e:
            print(f"Erro ao verificar conexão: {e}")
            return False

    @property
    def conn(self) -> Client:
        return self._conn


supabase = ClientSupabase(
    SupabaseConnection()
)