from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) - 1

        moved_index_sum = 0

        if moved_index_sum % target == 0:
            return True 
        



# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
        