from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        rn_cnt = Counter(ransomNote)
        mg_cnt = Counter(magazine)
        
        for key in rn_cnt.keys():
            if rn_cnt[key] <= mg_cnt[key]:
                continue
            else:
                return False
        
        return True
    
# ref: https://stackoverflow.com/questions/19883015/python-collections-counter-vs-defaultdictint
