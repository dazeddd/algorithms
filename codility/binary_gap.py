# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
"""
def solution(N):
    # Implement your solution here

    binary_text = bin(N).replace('0b','')
    # print(binary_text)

    max_count = 0
    count=0
    for num_char in binary_text:
        if num_char == '1':
            if max_count < count:
                max_count = count
            count = 0
        else:
            count += 1

    # print(max_count)
    return max_count
    

if __name__ == "__main__":
    # solution(N=20)
    # solution(N=1041)
    # solution(N=561892)
    solution(N=74901729)