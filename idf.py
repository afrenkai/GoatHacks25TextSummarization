# formula: log(num sentences/sentences with word)
import math
from typing import List, Dict

def computeIDF(wordLists: List[List[str]]) -> Dict[str, float]:
    idf_scores: Dict[str, float] = {}
    total_sentences: int = len(wordLists)

    for words in wordLists:
        for word in set(words):
            if word in idf_scores:
                idf_scores[word] += 1
            else:
                idf_scores[word] = 1
    
    for word in idf_scores:
        idf_scores[word] = math.log(total_sentences / idf_scores[word])
    return idf_scores

# def computeIDFSafer(wordLists:List[List[str]]) -> Dict[str, float]:
#     idf_scores: Dict[str,float] = {}
#     total_sentences: int = len(wordLists)

#     for words in wordLists:
#         for word in set(words):
#             idf_scores[word] = idf_scores.get(word,0) +1

#     for word in idf_scores:
#         idf_scores[word] = math.log (total_sentences / idf_scores[word])
    
    
#     return idf_scores
