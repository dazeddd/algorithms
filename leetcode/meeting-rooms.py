from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        # print(intervals)

        for idx in range(len(intervals)-1):
            if intervals[idx][1] > intervals[idx+1][0]:
                return False
            else:
                continue
        return True

if __name__ == "__main__":
    sol = Solution()
    # result = sol.canAttendMeetings(intervals=[[0,30],[5,10],[15,20]])
    result = sol.canAttendMeetings(intervals=[[7,10],[2,4]])
    print(result)