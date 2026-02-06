from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = list(range(len(nums)+1))

        # print(total)
        # print(nums.sort())

        nums.sort()
        zipped = zip(total, nums)
        for a, b in zipped:
            # print(pair)
            if a != b:
                return a

        return len(nums)
    

if __name__ == "__main__":
    sol = Solution()
    # sol.missingNumber(nums=[3,0,1])
    result = sol.missingNumber(nums=[9,6,4,2,3,5,7,0,1])
    # result = sol.missingNumber(nums=[0,1])
    print(result)


    # Input: nums = [3,0,1]
    # Output: 2


    # Input: nums = [9,6,4,2,3,5,7,0,1]
    # Output: 8