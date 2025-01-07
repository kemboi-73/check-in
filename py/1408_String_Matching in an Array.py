class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Initialize an empty list to store substrings
        result = []
        
        # Iterate through all pairs of words
        for i, word in enumerate(words):
            for j, other_word in enumerate(words):
                # Check if `word` is a substring of `other_word` and they are not the same word
                if i != j and word in other_word:
                    result.append(word)
                    break  # Break to avoid duplicates in the result
        
        return result
