# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    for i in range(0, K): 
        if A == []: 
            return A 
        A.insert(0, A.pop()) 
    return A 

if __name__ == "__main__":
    # result = solution([1, 2, 3, 4], 4)
    result = solution([3, 8, 9, 7, 6], 3)
    print(result)