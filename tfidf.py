from typing import Dict, List

def computeTFIDF(tfScoresList:List[Dict[str, float]], idfScores:Dict[str, float]) -> List[float]:
    tf_idf_sentences : List[float] = []
    for tf_scores in tfScoresList:
        print(sum(tf_scores[word] * idfScores[word] for word in tf_scores))
        # tf_idf_score = sum(tf_scores[word] * idfScores[word] for word in tf_scores)
        # tf_idf_sentences.append(tf_idf_score)
    
    return tf_idf_sentences
