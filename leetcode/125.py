
class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## O(n) time and O(n) space
        new_str = ""

        for char in s:
            if char.isalnum():
                new_str += char.lower()
        return new_str == new_str[::-1]

        ## Improved solution using pointers though much more code
        ## O(n) time and O(1) space
        # left, right = 0, len(s) - 1

        # while left < right:

        #     while left < right and not self.alpha_num(s[left]):
        #         left += 1

        #     while right > left and not self.alpha_num(s[right]):
        #         right -= 1

        #     if s[left].lower() != s[right].lower():
        #         return False

        #     left += 1
        #     right -= 1

        # return True

    def alpha_num(self, letter):
        ## replacing inbuilt isalnum function
        ## ord() checks the ascii value

        return ((ord('A') <= ord(letter) <= ord('Z')) or
                (ord('a') <= ord(letter) <= ord('z')) or
                (ord('0') <= ord(letter) <= ord('9')))
        

if __name__ == '__main__':
    #assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    #print(Solution().isPalindrome("AmanaplanacanalPanama"))