# https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

from typing import List

# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         return

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start_candidates = []        
        station_cnt = len(gas) 
        for idx in range(station_cnt):
            if gas[idx] >= cost[idx]:
                start_candidates.append(idx)

        print(start_candidates)
        for candidate in start_candidates:
            remain_gas = 0
            
            position = candidate 
            for idx in range(station_cnt+1):
                cost_idx = (position-1) % station_cnt
                gas_idx = position % station_cnt
                if idx == 0:
                    remain_gas = remain_gas + gas[gas_idx] 
                elif idx == station_cnt:
                    remain_gas = remain_gas - cost[cost_idx]
                else:
                    remain_gas = remain_gas - cost[cost_idx] + gas[gas_idx] 
                print(remain_gas)
                position += 1
            if remain_gas >= 0:
                return candidate
            else:
                continue
        return -1
                

            
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.

if __name__ == "__main__":
    sol = Solution()
    # ret = sol.canCompleteCircuit(gas=[1,2,3,4,5], cost=[3,4,5,1,2])
    ret = sol.canCompleteCircuit(gas=[5,1,2,3,4], cost=[4,4,1,5,1])
    # print(ret)




