#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        res=[]
        for digit in digits:
            s+=str(digit)
        ans=str(int(s)+1)
        for i in ans:
            res.append(int(i))
        return res
        
        
        
       

s=Solution()
final=s.plusOne([1,2,3])
print(final)