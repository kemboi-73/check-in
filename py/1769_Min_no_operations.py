class Solution:
    def minOperations(self, boxes: str):
        n = len(boxes)
        answer = [0] * n

        # First pass: calculate operations from left to right
        balls = 0
        operations = 0
        for i in range(n):
            answer[i] += operations
            balls += int(boxes[i])
            operations += balls

        # Second pass: calculate operations from right to left
        balls = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += operations
            balls += int(boxes[i])
            operations += balls

        return answer

# Example usage:
solution = Solution()
print(solution.minOperations("110"))  # Output: [1,1,3]
print(solution.minOperations("001011"))  # Output: [11,8,5,4,3,4]
