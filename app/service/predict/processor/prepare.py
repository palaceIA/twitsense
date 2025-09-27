import pandas as pd
import spacy
import re 

from typing import Any, List,Union
from core.settings import configs

class Preprocessor:
    def __init__(self):
        self.nlp = spacy.load(configs.MODEL_SPACY)

    def fit(self, X: Union[pd.Series, pd.DataFrame, List[str]], y: Any = None) -> "Preprocessor":
        return self

    def transform(self, X: Union[pd.Series, pd.DataFrame, List[str]]) -> pd.Series:
        if isinstance(X, pd.DataFrame):
            texts = X["texto"]
        else:
            texts = pd.Series(X)

        return texts.apply(self._preprocess)

    def _preprocess(self, text: str) -> str:
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'http\S+|www.\S+', '', text)
        doc = self.nlp(text)
        tokens = [token.lemma_.lower().strip() for token in doc if token.text.strip()]
        
        return ' '.join(tokens)

preprocessor = Preprocessor()