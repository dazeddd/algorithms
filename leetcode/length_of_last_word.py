class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_char_stack = []

        s = s.strip()
        for idx in range(len(s)):
            char = s[-(idx+1)]
            if char != ' ':
                last_word_char_stack.append(char)
            else:
                break
            
        return len(last_word_char_stack)

if __name__ == "__main__":
    # s = "   fly me   to   the moon  "
    s = "Hello World"
    
    sol = Solution()
    output = sol.lengthOfLastWord(s)
    print(output)
    
    