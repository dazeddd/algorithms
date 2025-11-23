# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict
from typing import List
from math import ceil, floor

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        criteria = ceil(len(nums) / 2)

        dd = defaultdict(int)
        for num in nums:
            dd[num] += 1

        for key, value in dd.items():
            if value >= criteria:
                return key


if __name__ == "__main__":
    sol = Solution()
    key = sol.majorityElement(nums=[2,2,1,1,1,2,2])
    print(key)
