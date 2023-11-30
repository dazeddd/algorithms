from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort()
        strs.sort(key=len)
        # print(strs)

        common_prefix = ""

        for idx in range(len(strs[0])):
            unique_strs = list(set(map(lambda s: s[:idx+1], strs)))
            
            if len(unique_strs) == 1:
                # print(unique_strs)
                common_prefix = unique_strs[0]
                continue
            else:
                break 
        
        return common_prefix

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 
if __name__ == "__main__":
    sol = Solution()
    prefix = sol.longestCommonPrefix(strs=["flower","flow","flight"])
    print(prefix)