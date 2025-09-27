import joblib
import numpy as np

from typing import List

from tensorflow.keras.models import load_model #type:ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type:ignore


from .processor.prepare import  preprocessor , Preprocessor
from core.settings import configs

class Labels:
    labels = {
        0 : "neutro" , 
        1 : "negativo" , 
        2 : "irrelevante", 
        3 : "positivo"
    } 

class Predictor:
    def __init__(
        self,
        model_path: str,
        tokenizer_path: str,
        preprocessor: Preprocessor,
        max_len: int,
    ):
        self.model = load_model(model_path)
        self.tokenizer = joblib.load(tokenizer_path)
        self.preprocessor = preprocessor
        self.max_len = max_len
        self.labels = Labels.labels
    
    def _tokenize_and_pad(self, texts: List[str]) -> np.ndarray:
        sequences = self.tokenizer.texts_to_sequences(texts)
        padded = pad_sequences(sequences, maxlen=self.max_len, padding="post")
        return padded
    
    def predict(self, texts: List[str]) -> List[str]:
        processed_texts = self.preprocessor.transform(texts)
        X = self._tokenize_and_pad(processed_texts.tolist())
        data_input = np.array(X)
        preds = self.model.predict(data_input)
        predicted_index = int(np.argmax(preds[0]))
        pred_name = self.labels[predicted_index]
        return pred_name

predictor = Predictor(
    model_path=configs.MODEL_CLASSIFIER,
    tokenizer_path=configs.TOKENIZER,
    preprocessor=preprocessor,
    max_len=100
)