from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        first_char_map = defaultdict(list)
        second_char_map = defaultdict(list)

        zipped = zip(s, t)
        for pair in zipped:
            first_char_map[pair[0]].append(pair[1])
            second_char_map[pair[1]].append(pair[0])

        print(first_char_map)
        print(second_char_map)

        for value in first_char_map.values():
            if len(set(value)) != 1:
                return False
        
        for value in second_char_map.values():
            if len(set(value)) != 1:
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    answer = sol.isIsomorphic(s="foo", t="bar")
    # answer = sol.isIsomorphic(s="badc", t="baba")
    print(answer)