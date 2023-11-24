
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_length = len(needle)

        idx_range = len(haystack)- len(needle)+ 1
        for idx in range(idx_range):
            if haystack[idx: idx+window_length] == needle:
                return idx

        return -1
    
if __name__ == "__main__":
    sol = Solution()
    answer = sol.strStr(haystack="sadbutsad", needle="sad")
    print(answer)
        
        
        

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0


