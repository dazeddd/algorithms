class Solution:
    def reverse(self, x: int) -> int:
        tmp_str = str(x)

        if tmp_str[0] == '-':
            base = "-"
            tmp_str = str(x)[1:]
        else:
            base = ""
            tmp_str = str(x)
        
        for idx in range(len(tmp_str)):
            base += tmp_str[-idx-1]

        # print(base)
        reversed = int(base)
        if reversed < (2 ** 31) and reversed >= -(2 ** 31):
            return int(base)
        else: 
            return 0
    

    
if __name__ == "__main__":
    sol = Solution()
    result = sol.reverse(x=123)
    # result = sol.reverse(x=120)
    # result = sol.reverse(x=-123)
    print(result)
