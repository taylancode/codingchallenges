from codingchallenges.utils.decorators import Decorators as d
from collections import Counter

class Solution:
    @d.timer
    def isAnagram(self, s: str, t: str) -> bool:

        ## Way to reference n letters
        ## compare num of letters in each
        ## if container[letter] % 2 = 0 - exists in both

        ## Solution 1 - O(s+t) time
        if len(s) != len(t):
            return False

        cs, ct = {}, {}

        for i in range(len(s)):
            cs[s[i]] = 1 + cs.get(s[i], 0)
            ct[t[i]] = 1 + ct.get(t[i], 0)

        for c in cs:
            if cs[c] != ct.get(c, 0):
                return False
        return True

        ## Solution 2 - cheat method using collections
        ## return Counter(s) == Counter(t)

        ## Solution 3 - simple and lowest space complexity potentially O(1) but O(nlogn) time 
        #return sorted(s) == sorted(t)


if __name__ == '__main__':
    #assert Solution().containsDuplicate(s="asdsad" t="dsadsa") is True
    print(Solution().isAnagram(s="rrat", t="car"))
