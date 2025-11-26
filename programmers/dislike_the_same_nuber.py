# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    
    answer = []
    
    prior_number = 0
    
    for idx in range(len(arr)):
        current_number = arr[idx]
        
        if idx == 0:
            answer.append(current_number)
        else:
            if prior_number != current_number:
                answer.append(current_number)
            else:
                continue
        
        prior_number = current_number
        
    return answer
