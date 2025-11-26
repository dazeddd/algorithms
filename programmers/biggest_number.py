# https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3
from itertools import permutations

def solution(numbers):
    
    permute = permutations(numbers, len(numbers))

    result_numbers = []

    for per in permute:
        initial_number = ''
        for num in per:
            initial_number += str(num)
        print(initial_number) 

        result_numbers.append(int(initial_number))
    
    max_number = max(result_numbers)
    answer = str(max_number)
    return answer

if __name__ == "__main__":

    solution([6,10,2])
    # solution([0,10,2]) 