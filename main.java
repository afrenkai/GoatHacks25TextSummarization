import java.util.*;

public class TfidfSummarizer {
    private static final Set<String> STOPWORDS = new HashSet<>(Arrays.asList(
            "is", "a", "that", "it", "the", "of", "and", "to", "in", "on", "for", "with",
            "this", "as", "by", "an", "be", "or", "at", "from", "has", "its", "like",
            "so", "such", "if", "their", "these", "than", "but", "not", "are", "was"
    ));

    private static final String TEXT = ""

    private static List<String> splitIntoSentences(String text) {
        List<String> sentences = Arrays.asList(text.split("\\. "));
        List<String> cleanedSentences = new ArrayList<>();
        for (String sentence : sentences) {
            sentence = sentence.trim().replace(".", ""); 
            if (!sentence.isEmpty()) {
                cleanedSentences.add(sentence);
            }
        }
        return cleanedSentences;
    }

    private static List<String> splitIntoWords(String sentence) {
        List<String> words = new ArrayList<>();
        String[] wordArray = sentence.toLowerCase().replaceAll("[(),]", "").split("\\s+"); 
        for (String word : wordArray) {
            if (!STOPWORDS.contains(word) && !word.isEmpty()) {
                words.add(word);
            }
        }
        return words;
    }

    private static Map<String, Double> computeTF(List<String> wordList) {
        Map<String, Double> tfScores = new HashMap<>();
        int totalWords = wordList.size();

        for (String word : wordList) {
            tfScores.put(word, tfScores.getOrDefault(word, 0.0) + 1.0);
        }

        for (String word : tfScores.keySet()) {
            tfScores.put(word, tfScores.get(word) / totalWords);
        }

        return tfScores;
    }

    private static Map<String, Double> computeIDF(List<List<String>> wordLists) {
        Map<String, Integer> docCount = new HashMap<>();
        int totalSentences = wordLists.size();

        for (List<String> words : wordLists) {
            Set<String> uniqueWords = new HashSet<>(words); 
            for (String word : uniqueWords) {
                docCount.put(word, docCount.getOrDefault(word, 0) + 1);
            }
        }

        Map<String, Double> idfScores = new HashMap<>();
        for (String word : docCount.keySet()) {
            idfScores.put(word, Math.log((double) totalSentences / docCount.get(word)));
        }

        return idfScores;
    }

    private static List<Double> computeTFIDF(List<Map<String, Double>> tfScoresList, Map<String, Double> idfScores) {
        List<Double> tfIdfScores = new ArrayList<>();

        for (Map<String, Double> tfScores : tfScoresList) {
            double score = 0.0;
            for (String word : tfScores.keySet()) {
                if (idfScores.containsKey(word)) {
                    score += tfScores.get(word) * idfScores.get(word);
                }
            }
            tfIdfScores.add(score);
        }

        return tfIdfScores;
    }

    private static String summarizeText(String text, int numSentences) {
        List<String> sentences = splitIntoSentences(text);
        List<List<String>> wordLists = new ArrayList<>();

        for (String sentence : sentences) {
            wordLists.add(splitIntoWords(sentence));
        }

        List<Map<String, Double>> tfScoresList = new ArrayList<>();
        for (List<String> words : wordLists) {
            tfScoresList.add(computeTF(words));
        }

        Map<String, Double> idfScores = computeIDF(wordLists);
        List<Double> tfIdfScores = computeTFIDF(tfScoresList, idfScores);

        List<Map.Entry<String, Double>> sortedSentences = new ArrayList<>();
        for (int i = 0; i < sentences.size(); i++) {
            sortedSentences.add(new AbstractMap.SimpleEntry<>(sentences.get(i), tfIdfScores.get(i)));
        }

        sortedSentences.sort((a, b) -> Double.compare(b.getValue(), a.getValue())); // Sort in descending order

        StringBuilder summary = new StringBuilder();
        for (int i = 0; i < numSentences && i < sortedSentences.size(); i++) {
            summary.append(sortedSentences.get(i).getKey()).append(". ");
        }

        return summary.toString().trim();
    }

    public static void main(String[] args) {
        String summary = summarizeText(TEXT, 2);
        System.out.println("Summary: " + summary);
    }
}
