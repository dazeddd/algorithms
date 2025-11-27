# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         s_idx = 0
#         t_idx = 0

#         if s == '':
#             return True

#         sub_str = ""

#         # for _ in range(len(t)):
#         while s_idx < len(s) and t_idx < len(t):
            
#             if t[t_idx] == s[s_idx]:
#                 sub_str += t[t_idx]
#                 t_idx += 1
#                 s_idx += 1
#             else:
#                 t_idx += 1

#             print(s_idx, t_idx)

#             # if s_idx == len(s):
#             #     break
        
#         if sub_str == s:
#             return True
#         else:
#             return False

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        def rec_isSubsequence(left_index, right_index):
            # base cases
            if left_index == LEFT_BOUND:
                return True
            if right_index == RIGHT_BOUND:
                return False
            # consume both strings or just the target string
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1

            return rec_isSubsequence(left_index, right_index)

        return rec_isSubsequence(0, 0)

if __name__ == "__main__":

    sol = Solution()
    # answer = sol.isSubsequence(s = "b", t = "abc")
    answer = sol.isSubsequence(s = "axc", t = "ahbgdc")
    print(answer)
