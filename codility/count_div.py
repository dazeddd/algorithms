"""
https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # Implement your solution here

    # result = []
    # for num in range(A, B+1):
        # if num % K == 0:
        #     result.append(num)
        #     print(num//K)

    if A == B:
        if (A / K) < 1:
            return 0
        else:
            return 1    

    latter = 0
    if (A / K) < 1:
        latter = 0
    else:
        latter = (A // K) - 1

    result = (B//K) - latter
    return result

    # for num in range(A, B+1)
    # A // K
    # B // K

    # print(A // 17)
    # print(B // 17)

    # if A // K < 1:
    #     (A + K) // K

    # print(A//K)

if __name__ == "__main__":
    # ret = solution(6, 11, 2)
    ret = solution(A = 11, B = 345, K = 17)
    print(ret)
