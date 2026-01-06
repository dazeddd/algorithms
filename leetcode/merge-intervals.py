from typing import List

# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         intervals.sort(key=lambda x: x[0])
#         # for idx, interval in enumerate(intervals):
#         #     if interval[]

#         merged = []

#         for idx in range(len(intervals)-1):
#             # print(idx)
#             if intervals[idx][1] > intervals[idx+1][0]:
#                 merged.append([intervals[idx][0],intervals[idx+1][1]])
#             else:
#                 continue
#         print(merged)

#         return intervals
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    


if __name__ == "__main__":
    sol = Solution()
    result = sol.merge(intervals=[[1,3],[2,6],[8,10],[15,18]])
    print(result)