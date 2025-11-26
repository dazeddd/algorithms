# https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3

from collections import Counter

def solution(clothes):
    total_case = 1
    
    cnt = Counter([x[1] for x in clothes])
    for v in cnt.values():        
        total_case *= (v + 1)
        
    answer = total_case - 1
    return answer