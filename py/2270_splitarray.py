from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate total sum of the array
        prefix_sum = 0
        valid_splits = 0
        
        # Iterate through indices 0 to n-2
        for i in range(len(nums) - 1):
            prefix_sum += nums[i]  # Update prefix sum
            # Check if the prefix sum is greater than or equal to the remaining sum
            if prefix_sum >= (total_sum - prefix_sum):
                valid_splits += 1
        
        return valid_splits
