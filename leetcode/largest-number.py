from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums.sort(key=lambda x: int(str(x)[0]), reverse=True)
        print(nums)

        # nums.

        return
    
if __name__ == "__main__":
    sol = Solution()

    nums = [3,30,34,5,9]
    answer = sol.largestNumber(nums=nums)

    # assert answer
