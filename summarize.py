from typing import Dict, List
from util import splitIntoSentences, splitIntoWords
from tf import computeTF
from idf import computeIDF
from tfidf import computeTFIDF

def summarizeText(text:str, numSentencesTarget: int = 3) -> str:
    sentences: List[str] = splitIntoSentences(text)
    words_lists: List[List[str]] = [splitIntoWords(sentence) for sentence in sentences]

    tf_scores_list: List[Dict[str, float]] = [computeTF(words) for words in words_lists]
    idf_scores: Dict[str, float] = [computeIDF(words_lists)]
    tf_idf_scores:List[float] = computeTFIDF(tf_scores_list, idf_scores)

    top_sent_idxs: List[int] = sorted(range(len(tf_idf_scores)), key = lambda i : tf_idf_scores[i],
    reverse = True)[:numSentencesTarget]

    summary : str = "".join([sentences[i] for i in sorted(top_sent_idxs)])
    return summary