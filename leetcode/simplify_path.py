class Solution:
    def simplifyPath(self, path: str) -> str:

        element_stack = []
        elements = path.split('/')
        # print(elements)
        for idx, e in enumerate(elements):

            if e == '..':
                if element_stack:
                    element_stack.pop()

            elif e and e != '.':

                element_stack.append(e)
                # canonical_path += '/'
                # canonical_path += e
            else:
                continue        
            
        canonical_path = '/' + '/'.join(element_stack)

        # print(element_stack)
        # print(canonical_path)

        return canonical_path
    
if __name__ == "__main__":

    sol = Solution()
    sol.simplifyPath(path='/home/')
    sol.simplifyPath(path='/../')
    sol.simplifyPath(path='/home//foo/')
    sol.simplifyPath(path='/home//../')

# Example 1:

# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:

# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
# Example 3:

# Input: path = "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.