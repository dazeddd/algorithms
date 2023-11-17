# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0

        for j in range(len(nums)-1):
            if nums[j+1] == nums[j]:
                continue
            else:
                idx += 1
                nums[idx] = nums[j+1]

        return idx + 1