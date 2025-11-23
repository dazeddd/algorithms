# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[idx] = nums[j]
                idx += 1

        return idx


if __name__ == "__main__":
    sol = Solution()
    sol.removeElement(nums= [3,2,2,3], val= 3)