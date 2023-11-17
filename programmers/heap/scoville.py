# https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3

from heapq import heapify, heappush, heappop

def solution(scoville, K):
    
    mixed_value = 0
    mixed_cnt = 0
    
    heapify(scoville)
    min_value = heappop(scoville)
    
    loop_cnt = len(scoville)-1
    
    for i in range(loop_cnt):
        next_value = heappop(scoville)
        
        mixed_value = min_value + next_value * 2
        mixed_cnt += 1

        print(mixed_value)

        if mixed_value >= K:
            return mixed_cnt
        else: 
            heappush(scoville, mixed_value)
            continue
    
    return -1
        
if __name__ == "__main__":
    cnt = solution([1, 2, 3, 9, 10, 12], 7)
    # print(cnt)