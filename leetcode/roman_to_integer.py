
class Solution:
    def romanToInt(self, s: str) -> int:
        # IV, IX, XL, XC, CD, CM
        double_roman_integer_maps = {
            'IV': 4, 
            'IX': 9, 
            'XL': 40, 
            'XC': 90, 
            'CD': 400, 
            'CM': 900
        }
        single_roman_integer_maps = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        skip_idx = []
        values = []
        for idx, char in enumerate(s):
            if idx in skip_idx:
                continue

            if char in ('I','X','C'):
                if idx+1 < len(s) and s[idx]+s[idx+1] in double_roman_integer_maps.keys():
                    values.append(double_roman_integer_maps[s[idx]+s[idx+1]])
                    skip_idx.append(idx+1)
                else:
                    values.append(single_roman_integer_maps[s[idx]])
            else:
                values.append(single_roman_integer_maps[s[idx]])
            # print(idx, char)
        # print(values)
        result_value = sum(values)
        return result_value

        # for slicing_idx in range(len(s)):


if __name__ == "__main__":

    sol = Solution()
    # answer = sol.romanToInt(s='MCMXCIV')
    answer = sol.romanToInt(s='LVIII')

    # Input: s = "MCMXCIV"
    # Output: 1994