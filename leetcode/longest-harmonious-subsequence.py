from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:

        HS = []
        nums.sort()

        idxs = sorted(list(range(2, len(nums)+1)), reverse= True)
        # for idx in range(2, len(nums)+1):
        for idx in idxs:
            for p in range(len(nums)-(idx-1)):
                # print(idx,p)
                candidate_array = nums[p:p+idx]
                # print(candidate_array)

                # if max(candidate_array) - min(candidate_array) == 1:
                if candidate_array[-1] - candidate_array[0] == 1:
                    # HS.append(candidate_array)
                    return len(candidate_array)
                else:
                    continue

        # print(HS)
        # print(list(map(lambda x: len(x), HS)))
        # if HS:
        #     return len(HS[-1])
        # else:
        #     return 0
        
        return 0


if __name__ == "__main__":
    sol = Solution()
    result = sol.findLHS(nums=[1,3,2,2,5,2,3,7])
    print(result)
    
    # TO FIX
    # Some what limit exceeded...