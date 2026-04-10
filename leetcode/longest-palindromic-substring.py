

class Solution:
    def longestPalindrome(self, s: str) -> str:

        start_idx = 0
        end_idx = len(s)

        def check_palindrome(word: str):
            for i in range(len(word)// 2):
                if word[i] != word[-(i+1)]:
                    return False
            return True

        pds = []
        while end_idx > start_idx:

            for i in range(len(s[start_idx:])):
                tmp_s = s[start_idx:(end_idx-i)]
                # print(tmp_s)

                if check_palindrome(word=tmp_s):
                    pds.append(tmp_s)
                else: 
                    continue

            start_idx += 1

        # print(pds)
        # print(sorted(pds, key=lambda x: len(x))[-1])

        loggest_palindrome = sorted(pds, key=lambda x: len(x))[-1]

        # print(max(list(map(lambda x: len(x), pds))))
        # print(map(lambda x: len(x), pds))

        return loggest_palindrome
    

if __name__ == "__main__":
    sol = Solution()
    # result = sol.longestPalindrome(s="cbbd")
    result = sol.longestPalindrome(s="babad")
    print(result)