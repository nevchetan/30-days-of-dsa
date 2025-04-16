#to check if the given numer is palindrrome or not
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        return str(x) == str(x)[::-1]
sol=Solution()
x=121
res=sol.isPalindrome(x)
print(res)