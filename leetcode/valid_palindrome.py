class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check_str = ""

        for char in s:
            if not char.isalnum():
                continue
            else:
                check_str += char.lower()

        check_cnt = len(check_str) // 2
        for i in range(check_cnt):
            if (check_str[i] == check_str[-(i+1)]):
                continue
            else:
                return False
        
        return True

        # return check_str

if __name__ == "__main__":

    # Input: s = "A man, a plan, a canal: Panama"
    s = " "

    sol = Solution()
    # check_str = sol.isPalindrome(s)
    # print(check_str)
    result = sol.isPalindrome(s)
    print(result)