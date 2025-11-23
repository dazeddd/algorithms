class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0

        if s == '':
            return True

        sub_str = ""

        # for _ in range(len(t)):
        while s_idx < len(s) and t_idx < len(t):
            
            if t[t_idx] == s[s_idx]:
                sub_str += t[t_idx]
                t_idx += 1
                s_idx += 1
            else:
                t_idx += 1

            print(s_idx, t_idx)

            # if s_idx == len(s):
            #     break
        
        if sub_str == s:
            return True
        else:
            return False

if __name__ == "__main__":

    sol = Solution()
    # answer = sol.isSubsequence(s = "b", t = "abc")
    answer = sol.isSubsequence(s = "axc", t = "ahbgdc")
    print(answer)
