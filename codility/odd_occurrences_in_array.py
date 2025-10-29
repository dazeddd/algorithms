from collections import Counter

def solution(A):
    # Implement your solution here
    for key, value in Counter(A).items():
        if value % 2 == 1:
            return key
        else:
            continue

if __name__ == "__main__":

    A = [9,3,9,3,9,7,9]

    result = solution(A)
    print(result)

