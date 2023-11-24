# https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]

        # if index start at gas[0]
        remain = 0

        # remain += gas[3]
        # remain - cost[3] + gas[4]
        
        remain += gas[0]
        remain - cost[0] + gas[1]
        remain - cost[1] + gas[2]
        remain - cost[2] + gas[3]
        remain - cost[3] + gas[4]
        remain - cost[4]

        print(remain)

        # for i in range(len(gas)):
        for i in range(1):
            remain = 0
            remain += gas[0]
            remain - cost[0] + gas[1]
            remain - cost[1] + gas[2]
            remain - cost[2] + gas[3]
            remain - cost[3] + gas[4]
            remain - cost[4]



if __name__ == "__main__":
    sol = Solution()
    sol.canCompleteCircuit(gas=[1,2,3,4,5], cost=[3,4,5,1,2])



