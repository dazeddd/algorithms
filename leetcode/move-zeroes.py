from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        start_idx = 0
        end_idx = len(nums)

        for i in range(len(nums)):
            try:
                del_idx = nums[start_idx:end_idx-i].index(0)
                del nums[del_idx]
                nums.append(0)
            except ValueError:
                break

        # print(nums)
        # del nums[nums.index(0)]
        # nums.append(0)
        # print(nums)

        # Memory good
        # Runtime not good


if __name__ == "__main__":
    sol = Solution()
    # sol.moveZeroes(nums=[0,1,0,3,12])
    sol.moveZeroes(nums=[0])