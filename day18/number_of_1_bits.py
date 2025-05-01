#In this question we have given anumber and we have to show output as the number or count of 1 bits in it 


class Solution:
    def hammingWeight(self, n: int) -> int:
        rem=0
        q=0
        res=[]
        while n!=0:
            q=n//2
            rem=int(n%2)
            n=q
            res.append(rem)
            
        return res.count(1)

        

sol=Solution()
n=11
res=sol.hammingWeight(n)
print(res)