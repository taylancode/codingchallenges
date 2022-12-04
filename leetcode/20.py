from codingchallenges.utils.decorators import Decorators as d
from typing import List

class Solution:
    @d.timer
    def isValid(self, s: str) -> bool:

        ## O(n) time and memory
        ## Create a stack
        ## if opening brackets, add to stack
        ## if top of stack is closing for start, pop the last entry
        ## if remaining entries in list, return False

        stack = []
        dic = {
            '}': '{',
            ']': '[',
            ')': '('
            }

        for x in s:
            if x in dic:
                if stack and stack[-1] == dic[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)

        return True if not stack else False

if __name__ == '__main__':
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("{}") is True
    assert Solution().isValid("()[]}") is False
    assert Solution().isValid("([)]]{}") is False
    assert Solution().isValid("(") is False

