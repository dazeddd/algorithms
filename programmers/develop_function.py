# https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3

def solution(progresses, speeds):
    
    answer = []
    
    while progresses:
        
        function_cnt = 0
        
        for idx in range(len(progresses)):
            progresses[idx] += speeds[idx]
            
        while progresses and (progresses[0] >= 100):
            progresses.pop(0)
            speeds.pop(0)
            function_cnt += 1
            
        if function_cnt:
            answer.append(function_cnt)
        else:
            continue

        # print(progresses)
        
    return answer

if __name__ == "__main__":

    answer = solution([93, 30, 55], [1, 30, 5])
    print(answer)