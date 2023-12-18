
# sliding window 가 two pointer 와 다른 점은 구간의 길이가 고정되어 있다는 것이다.

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        nums_length = len(nums)
        
        start = 0 
        window_length = 1


        # for i in range(nums_length):

            # print(nums[i: i + window_length])


        
        sub_array = nums[start: start + window_length]
        if sum(sub_array) >= target:
            return window_length
        
        window_length += 1
            

        return 0



        # Time Limit Exceeded
        # nums_length = len(nums)
        # # minimum_length = len(nums)
        # subarray_length = []
        
        # for i in range(nums_length):
        #     for j in range(nums_length-i):
        #         sub_array = nums[i: i+j+1]
        #         if sum(sub_array) >= target:
        #             # print(i, j)
        #             # print(sub_array)
        #             subarray_length.append(len(sub_array))

        # if subarray_length:
        #     return min(subarray_length)
        # else:
        #     return 0

        return
                    

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]

    sol = Solution()
    answer = sol.minSubArrayLen(target=target, nums=nums)
    # print(answer)
    
        