import math
from typing import List, Dict

STOPWORDS = set([
    "is", "a", "that", "it", "the", "of", "and", "to", "in", "on", "for", "with",
    "this", "as", "by", "an", "be", "or", "at", "from", "has", "its", "like",
    "so", "such", "if", "their", "these", "than", "but", "not", "are", "was"
])

TEXT = '''
The dominant sequence transduction models are based on complex recurrent or 
convolutional neural networks in an encoder-decoder configuration. 
The best performing models also connect the encoder and decoder through 
an attention mechanism. We propose a new simple network architecture, 
the Transformer, based solely on attention mechanisms, 
dispensing with recurrence and convolutions entirely. 
Experiments on two machine translation tasks show these models to 
be superior in quality while being more parallelizable and requiring 
significantly less time to train. Our model achieves 28.4 BLEU 
on the WMT 2014 English-to-German translation task, improving 
over the existing best results, including ensembles by over 2 BLEU. 
On the WMT 2014 English-to-French translation task, 
our model establishes a new single-model state-of-the-art 
BLEU score of 41.8 after training for 3.5 days on eight GPUs, 
a small fraction of the training costs of the best models from
the literature. We show that the Transformer generalizes well 
to other tasks by applying it successfully to English 
constituency parsing both with large and limited training data. 
'''



def split_into_sentences(text: str) -> List[str]: 
    '''
    Splits a given corpus (piece of text ) into sentences, which are treated as lists of strings

    Param(s): 
        text (String) : Input corpus to be split into sentences
    
    Returns:
        List[str]: List of sentences extracted from the input text 
    '''

    pass

def split_into_words(sentence: str) -> List[str]:
    '''
    Splits a given sentence into individual words, removing words that fall into our defined stopwords
    (see above) or are punctuation.

    Param(s):
        sentence (String) : input sentence to be "tokenized" (cleaned) into words
    
    Returns:
        List[str]: A list of words in the sentence after "tokenization"
    '''
    pass

# formula : count of word in sentence / total words in sentence

def compute_tf(word_list: List[str]) -> Dict[str, float]:
    '''
    Computes Term Frequency (TF) for each word in a given sentence

    Formula: 
        TF = (count of word in sentence) / (total words in sentence)

    Param(s):
        word_list (List[str]): list of words from a sentence

    Returns:
        Dict[str, float]: A dictionary where the key is the word and the value is the term frequency score
    '''
    pass

# formula: log(num sentences / num sentences with word)
def compute_idf(word_lists: List[List[str]]) -> Dict[str, float]:
    '''
    Computes Inverse Document Frequency (IDF) of words across multiple sentences

    Formula:
        IDF = log((Number of Sentences) / (Number of Sentences with the word in it))

    Param(s):
        word_lists (List[List[str]]): list of word lists, where each list represents words from a sentence

    Returns:
        Dict[str, float]: a dictionary where the keys are the words and the values are their IDF scores
    '''
    
    pass

# formula pretty easy, just TF * IDF for each instance of word in sentence.

def compute_tf_idf(tf_scores_list: List[Dict[str, float]], idf_scores: Dict[str, float]) -> List[float]:
    '''
    Computes the Term Frequency-Inverse Document Frequency (TF-IDF) Scores for each sentence

    Formula:
        TF-IDF = TF * IDF

    Param(s):
        tf_scores_list(List[Dict[str, float]]): List of dicts containing tf scores per sentence
        idf_scores (Dict[str, float]) : Dict of IDF scores for all words

    Returns: 
        List[float]: list of TF-IDF scores for each sentence
    '''
    pass

def summarize_text(text: str, num_sentences: int = 3) -> str:
    '''
    Generates a summary of the input text by selecting the most important sentences
    (Those with highest TF-IDF scores)

    Param(s):
        text (str) : text to summarize
        num_sentences: number of sentences to limit the summary to

    Returns:
    str: String containing the summarized text. 
    '''
    pass


summary = summarize_text(text = TEXT, num_sentences=2)

print("Summary:", summary)
