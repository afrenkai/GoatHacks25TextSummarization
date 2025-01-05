import java.util.*;

public class TfidfSummarizer {
    private static final Set<String> STOPWORDS = new HashSet<>(Arrays.asList(
            "is", "a", "that", "it", "the", "of", "and", "to", "in", "on", "for", "with",
            "this", "as", "by", "an", "be", "or", "at", "from", "has", "its", "like",
            "so", "such", "if", "their", "these", "than", "but", "not", "are", "was"
    ));

    private static final String TEXT = "The dominant sequence transduction models are based on complex recurrent or 
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
    constituency parsing both with large and limited training data."

    private static List<String> splitIntoSentences(String text) {
    }

    private static List<String> splitIntoWords(String sentence) {
    }

    private static Map<String, Double> computeTF(List<String> wordList) {
    }

    private static Map<String, Double> computeIDF(List<List<String>> wordLists) {
    }

    private static List<Double> computeTFIDF(List<Map<String, Double>> tfScoresList, Map<String, Double> idfScores) {
    }

    private static String summarizeText(String text, int numSentences) {
    // prob use string builder after computing scores. use a little bit of sorting to return numSentences sentences
    }

    public static void main(String[] args) {
        String summary = summarizeText(TEXT, 2);
        System.out.println("Summary: " + summary);
    }
}
