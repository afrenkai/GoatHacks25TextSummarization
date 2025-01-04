# formula: num of word in sentence / total words in sentence
from typing import List, Dict

def computeTF(wordsList: List[str]) -> Dict[str, float]:
    tf_scores = {}
    total_words = len(wordsList)

    for word in wordsList:
        if word in tf_scores:
            tf_scores[word] += 1
        else:
            tf_scores[word] = 1
    for word in tf_scores:
        tf_scores[word]/= total_words
    
    return tf_scores

def computeTFSafer(wordsList:List[str]) -> Dict[str, float]:
    tf_scores:Dict[str, float] = {}
    total_words = len(wordsList)

    for word in wordsList:
        tf_scores[word] = tf_scores.get(word,0) + 1
    
    for word in tf_scores:
        tf_scores[word] /= total_words
    
    return tf_scores

