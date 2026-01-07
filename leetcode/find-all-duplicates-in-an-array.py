from collections import defaultdict
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Counter 말고?
        dups = []
        num_cnt = defaultdict(int)
        for num in nums:
            num_cnt[num] += 1

        for key, value in num_cnt.items():
            if value == 2:
                dups.append(key)

        return dups


if __name__ == "__main__":
    sol = Solution()
    result = sol.findDuplicates(nums=[4,3,2,7,8,2,3,1])
    print(result)