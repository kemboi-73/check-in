class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        # Initialize a counter for the prefix matches
        count = 0
        
        # Iterate through each word in the list
        for word in words:
            # Check if the word starts with the prefix
            if word.startswith(pref):
                count += 1
        
        # Return the total count
        return count
