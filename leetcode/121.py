from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        ## O(n) time and O(1) space

        maxprof = 0
        buy, sell = 0, 1

        while sell < len(prices):

            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxprof = max(maxprof, profit)
            else:
                buy = sell

            sell += 1

        return maxprof



if __name__ == '__main__':
    #assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    print(Solution().maxProfit([7,1,5,3,6,4]))
    #print(Solution().isPalindrome("AmanaplanacanalPanama"))