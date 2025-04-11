#here we have two strings and we have to check whether the another string is substring of the other or not with a proper sequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        for char in t:
            if i<len(s) and s[i]==char:
                i+=1
        return i==len(s)
        
        
        

        
sol=Solution()
s="abc"
t="ambcnd"
res=sol.isSubsequence(s,t)
print(res)        
        
        