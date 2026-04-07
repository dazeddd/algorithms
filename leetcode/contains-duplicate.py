from typing import List
# from collections import Counter
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dd = defaultdict(int)
        # dd[]
        for num in nums:
            if dd[num] == 1:
                return True
            else:
                dd[num] += 1

        # print(dd)

        # for key, value in dd.items():
        #     if value > 1:
        #         return True
        return False
    

if __name__ == "__main__":
    sol = Solution()
    result = sol.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2])
    print(result)