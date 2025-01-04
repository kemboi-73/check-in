class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Dictionary to store the first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}
        
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i
        
        unique_palindromes = set()

        # Iterate over all characters
        for char in first_occurrence:
            start = first_occurrence[char]
            end = last_occurrence[char]
            # Check if there is room for characters in the middle
            if end - start > 1:
                # Add all unique middle characters to form palindromes
                middle_chars = set(s[start + 1:end])
                for middle_char in middle_chars:
                    unique_palindromes.add((char, middle_char, char))
        
        return len(unique_palindromes)
