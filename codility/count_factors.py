# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/count_factors/
"""

def solution(N):
    # Implement your solution here

    factors = []
    for i in range(N):

        if (N % (i+1) == 0) and (i+1 in factors):
            break

        if (N % (i+1) == 0):
            if i+1 == N//(i+1):
                factors.append(i+1)
            else:
                factors.append(i+1)
                factors.append(N//(i+1))
        else:
            continue

    # print(factors)
    return len(factors)

if __name__ == "__main__":
    solution(N=25)