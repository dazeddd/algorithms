class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s_array = s.split(' ')
        print(s_array)

        if len(s_array) != len(pattern):
            return False

        matching_dict = {}
        result_array = []

        for idx, value in enumerate(pattern):
            print(idx)
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



if __name__ == "__main__":
    sol = Solution()
    # answer = sol.wordPattern(pattern='abba', s='dog dog dog dog')
    answer = sol.wordPattern(pattern='abba', s="dog cat cat fish")
    # answer = sol.wordPattern(pattern='jquery', s='jquery')
    print(answer)

    # Wow 100% Runtime beats...