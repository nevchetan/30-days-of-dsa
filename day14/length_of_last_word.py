class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st_list=s.split()
        return(len(st_list[-1]))
        
        

        
sol=Solution()
s="hello, wasssup"
res=sol.lengthOfLastWord(s)
print(res)