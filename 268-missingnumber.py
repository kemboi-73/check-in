class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # s = set(nums)

        
        # for num in range (n+1):
        #     if num not in s:
        #         return num

        # optimized to 0(1) time complexity
        n = len(nums)
        expected = n * (n+1)//2
        return expected - sum(nums)

        
