import joblib
import numpy as np
from tensorflow.keras.models import load_model #type:ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences  #type:ignore

class TextClassifier:
    def __init__(self, model_path: str, tokenizer_path: str, max_len: 100):

        self.model = load_model(model_path)
        self.tokenizer = joblib.load(tokenizer_path)
        self.max_len = max_len

classifier = TextClassifier()