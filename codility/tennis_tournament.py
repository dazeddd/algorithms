"""
https://app.codility.com/programmers/trainings/3/tennis_tournament/
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, C):
    # Implement your solution here

    if P >= C * 2:
        return C
    else:
        return P // 2

    # pass

if __name__ == "__main__":
    # ret = solution(10,3)
    ret = solution(5,3)
    print(ret)


