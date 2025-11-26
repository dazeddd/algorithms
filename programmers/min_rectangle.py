# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):

    width = 0
    height = 0

    for w, h in sizes:
        # print(w, h)
        if w < h:
            w, h = h, w
        width = max(width, w)
        height = max(height, h)
            
    answer = width * height
    return answer

if __name__ == "__main__":
    answer = solution(sizes=[[60, 50], [30, 70], [60, 30], [80, 40]])
    print(answer)

[[60, 50], 
 [30, 70],
 [60, 30],
 [80, 40]]

