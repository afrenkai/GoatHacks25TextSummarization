from constants import STOPWORDS
from typing import List, Dict
def splitIntoSentences(text:str) -> List[str]:
    sentences = text.split('. ')
    sentences = [sentence.strip().replace(".", "") for sentence in sentences if sentence]
    return sentences 

def splitIntoWords(sentence:str)-> List[str]:
    words = sentence.lower().replace("(","").replace(")", "").replace(",","").split()
    return [word for word in words if word not in STOPWORDS]
