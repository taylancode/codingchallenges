from codingchallenges.utils.decorators import Decorators as d
from typing import List

class Solution:
    @d.timer
    def containsDuplicate(self, nums: List[int]) -> bool:

        container = set()

        for num in nums:
            if num not in container:
                container.add(num)
            else:
                return True
        return False

if __name__ == '__main__':
    assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) is True
