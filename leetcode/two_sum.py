from typing import List
import itertools

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # idxs = list(range(len(nums)))
        # idx_cmbs = list(itertools.combinations(idxs, 2))

        # for cmb in idx_cmbs:
        #     if sum([nums[c] for c in cmb]) == target:
        #         return cmb

        num_map = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [idx, num_map[complement]]
            
            num_map[num] = idx
        
        return []
            

if __name__ == "__main__":
    sol = Solution()
    answer = sol.twoSum(nums = [2,7,11,15], target = 9)
    print(answer)
