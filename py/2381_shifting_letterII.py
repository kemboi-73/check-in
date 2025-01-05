class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Convert the string to a list of characters for easy manipulation
        s = list(s)
        # Initialize an array to track the net shifts at each index
        shift_counts = [0] * (len(s) + 1)

        # Populate the shift_counts array based on the shifts
        for start, end, direction in shifts:
            if direction == 1:
                shift_counts[start] += 1
                shift_counts[end + 1] -= 1
            else:
                shift_counts[start] -= 1
                shift_counts[end + 1] += 1

        # Calculate the cumulative shifts
        cumulative_shift = 0
        for i in range(len(s)):
            cumulative_shift += shift_counts[i]
            shift_counts[i] = cumulative_shift

        # Apply the shifts to the characters in the string
        for i in range(len(s)):
            new_char_index = (ord(s[i]) - ord('a') + shift_counts[i]) % 26
            s[i] = chr(ord('a') + new_char_index)

        # Join the list back into a string and return
        return ''.join(s)
