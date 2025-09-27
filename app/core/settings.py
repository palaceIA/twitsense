from pydantic_settings import (
    BaseSettings, 
    SettingsConfigDict
)
from dotenv import load_dotenv
import os 

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))
class Configs(BaseSettings):
    
    SUPABASE_URL:str = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY :str = os.environ.get("SUPABASE_KEY")
    MODEL_SPACY : str = os.environ.get("MODEL_SPACY")
    MODEL_CLASSIFIER : str = os.environ.get("MODEL_CLASSIFIER")
    TOKENIZER : str = os.environ.get("TOKENIZER")
    model_config = SettingsConfigDict(env_file=".env")  

configs = Configs()
