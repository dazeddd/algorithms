from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:        
        max_area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            width = end - start
            max_area = max(max_area, min(height[start], height[end])*width)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return max_area

if __name__ == "__main__":

    # Input: height = [1,8,6,2,5,4,8,3,7]
    # Output: 49

    sol = Solution()
    ma = sol.maxArea([1,8,6,2,5,4,8,3,7])
