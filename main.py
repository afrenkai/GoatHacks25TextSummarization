import math
from typing import List, Dict

STOPWORDS = set([
    "is", "a", "that", "it", "the", "of", "and", "to", "in", "on", "for", "with",
    "this", "as", "by", "an", "be", "or", "at", "from", "has", "its", "like",
    "so", "such", "if", "their", "these", "than", "but", "not", "are", "was"
])

TEXT = '''
Just installed LazyVim and liking it quite a bit, though I don't understand how to switch between open tabs.

It seems like <leader>-<tab>-[ or <leader>-<tab>-] should do it, but after I hit '[' or ']' the popup menu simply goes away instead of actually switching to a different open tab. By contrast, <leader>-<tab>-<tab> will create a new tab, and <leader>-<tab>-d will delete the current tab.

Am I misunderstanding how this feature is supposed to work?

(I searched for this and didn't find anything recent or specific so maybe I'm doing something wrong)

[edit] so, yes, it is a misunderstanding on my part. What appear as "tabs" across the top of the screen are not neovim tabs, but visual representations of open buffers. Which, yes, look visually like "tabs," but they're not actual vim tabs. So the way to move between "tabs" (buffers) in LazyVim using the default keymaps is <S-h> and <S-l>.

*Actual* neovim tabs have some shortcuts via the <leader><tab> sequence. When you create a new tab in lazyvim (<leader><tab><tab>) it and other tabs will appear to the right of the open buffers along the top of the screen as numbered ui-widgets-which-look-like-tabs-but-need-a-different-name-since-its-confusing.

TLDR: <S-h>, <S-l> and what I'm calling tabs are actually buffers

'''



def split_into_sentences(text: str) -> List[str]:
    sentences = text.split('. ')
    sentences = [sentence.strip().replace(".", "") for sentence in sentences if sentence]
    return sentences

def split_into_words(sentence: str) -> List[str]:
    words = sentence.lower().replace("(", "").replace(")", "").replace(",", "").split()
    return [word for word in words if word not in STOPWORDS]  # Remove stopwords

# formula : count of word in sentence / total words in sentence
def compute_tf(word_list: List[str]) -> Dict[str, float]:
    tf_scores: Dict[str, float] = {}
    total_words: int = len(word_list)

    for word in word_list:
        tf_scores[word] = tf_scores.get(word, 0) + 1

    for word in tf_scores:
        tf_scores[word] /= total_words  # apply formula

    return tf_scores

# formula: log(num sentences / num sentences with word)
def compute_idf(word_lists: List[List[str]]) -> Dict[str, float]:
    idf_scores: Dict[str, float] = {}
    total_sentences: int = len(word_lists)

    for words in word_lists:
        for word in set(words):  
            idf_scores[word] = idf_scores.get(word, 0) + 1

    for word in idf_scores:
        idf_scores[word] = math.log(total_sentences / idf_scores[word])  #apply formula

    return idf_scores

# formula pretty easy, just TF * IDF for each instance of word in sentence.

def compute_tf_idf(tf_scores_list: List[Dict[str, float]], idf_scores: Dict[str, float]) -> List[float]:
    return [sum(tf_scores[word] * idf_scores[word] for word in tf_scores) for tf_scores in tf_scores_list]


def summarize_text(text: str, num_sentences: int = 3) -> str:
    sentences = split_into_sentences(text)
    word_lists = [split_into_words(sentence) for sentence in sentences]

    tf_scores_list = [compute_tf(words) for words in word_lists]
    idf_scores = compute_idf(word_lists)
    tf_idf_scores = compute_tf_idf(tf_scores_list, idf_scores)

    sorted_sentences = sorted(zip(sentences, tf_idf_scores), key=lambda x: x[1], reverse=True)

    summary_sentences = [sentence for sentence, _ in sorted_sentences[:num_sentences]]

    return " ".join(summary_sentences)

summary = summarize_text(TEXT, num_sentences=2)
print("Summary:", summary)
