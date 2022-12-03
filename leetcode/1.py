from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ## if target - num in hashmap
        ## hashmap needed to avoid O(n2) time
        ## O(n) space since we will add all n in hashmap
        numhash = {}

        for idx, num in enumerate(nums):
            targetn = target-num
            if targetn in numhash:
                return [numhash[targetn], idx]
            numhash[num] = idx

if __name__ == '__main__':
    print(Solution().twoSum([3,3], 6))