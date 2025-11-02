from collections import defaultdict

"""
https://app.codility.com/programmers/lessons/8-leader/dominator/
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    idxs = defaultdict(list)
    if not A:
        return -1

    for idx in range(len(A)):
        idxs[A[idx]].append(idx)

    if len(A) != 1 and len(set(map(len, idxs.values()))) == 1:
        return -1

    dominator = 0
    max_length = 0
    for key, value in idxs.items():
        if max_length < len(value):
            dominator = key
            max_length = len(value)
        else:
            continue
    
    # print(idxs[dominator])
    return idxs[dominator][0]

    # print(idxs)
    # print(dominator)
    # print(max_length)
    # pass


if __name__ == "__main__":
    solution(A=[3,4,3,2,3,-1,3,3])