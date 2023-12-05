# from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_array = s.split(' ')

        matching_dict = {}
        result_array = []

        for idx, value in enumerate(pattern):
            if value in matching_dict:
                result_array.append(matching_dict[value])
            else:
                matching_dict[value] = s_array[idx]
                result_array.append(s_array[idx])
        
        result_str = " ".join(result_array)
        
        # print(matching_dict)
        # print(result_array)        
        # print(result_str)

        if len(set(matching_dict.keys())) != len(set(matching_dict.values())):
            return False
        
        if s == result_str:
            return True
        else:
            return False


        # dd = defaultdict(list)
        # for idx, value in enumerate(pattern):
        #     dd[value].append(s_array[idx])
        # print(dd)
        
        # if len(set(dd.keys())) != len(set(dd.values())):
        #     return False
        
        # for value in dd.values():
        #     if len(set(value)) == 1:
        #         continue
        #     else:
        #         return False
            
        # return True


if __name__ == "__main__":
    sol = Solution()
    answer = sol.wordPattern(pattern='abba', s='dog dog dog dog')
    print(answer)
