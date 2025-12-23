from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        # print(count)
        # print(count.get)
        return heapq.nlargest(k, count.keys(), key=count.get) 
    

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    
    sol = Solution()
    sol.topKFrequent(nums=nums, k=k)