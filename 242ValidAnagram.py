class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # return s==t
# reduces time complexity by use of counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t
