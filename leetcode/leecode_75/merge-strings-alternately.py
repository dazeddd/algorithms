class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_turns = min(len(word1), len(word2))

        result_str = ''
        last_idx = 0
        for idx in range(min_turns):
            result_str += word1[idx]
            result_str += word2[idx]

            last_idx = idx

        diff = len(word1) - len(word2)
        if diff > 0:
          result_str += word1[last_idx+1:]  
        elif diff < 0:
          result_str += word2[last_idx+1:]  
        else:
            pass
        
        return result_str
    
if __name__ == "__main__":
   
   print(__name__)

   sol = Solution()
   result_str = sol.mergeAlternately(word1='ab', word2='pqrs')
   print(result_str)