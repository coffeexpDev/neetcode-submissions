class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comap = {
            "}": "{", 
            ")": "(",
            "]": "["
            }

        for c in s:
            if c in comap:
                if stack and stack[-1] == comap[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False
        