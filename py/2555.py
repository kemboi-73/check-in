from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Helper function to check if a word starts and ends with a vowel
        def is_vowel_string(word: str) -> bool:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return word[0] in vowels and word[-1] in vowels
        
        # Step 1: Build the prefix sum array
        n = len(words)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if is_vowel_string(words[i]) else 0)
        
        # Step 2: Process the queries
        result = []
        for li, ri in queries:
            result.append(prefix[ri + 1] - prefix[li])
        
        return result

# Example usage:
# words = ["aba", "bcb", "ece", "aa", "e"]
# queries = [[0, 2], [1, 4], [1, 1]]
# solution = Solution()
# print(solution.vowelStrings(words, queries))  # Output: [2, 3, 0]
