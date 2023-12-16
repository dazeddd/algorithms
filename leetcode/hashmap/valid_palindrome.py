from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dd = defaultdict(int)
        t_dd = defaultdict(int)
        
        for char in s:
            s_dd[char] += 1
        for char in t:
            t_dd[char] += 1
        
        # print(s_dd)
        # print(t_dd)

        return (s_dd == t_dd)

if __name__ == "__main__":
    s = 'anagram'
    t = 'nagaram'
    
    sol = Solution()
    answer = sol.isAnagram(s=s, t=t)
    print(answer)

