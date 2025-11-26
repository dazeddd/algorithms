# https://school.programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    
    for cm in commands:
        sliced_array = sorted(array[cm[0]-1:cm[1]])
        answer.append(sliced_array[cm[2]-1])

    return answer

