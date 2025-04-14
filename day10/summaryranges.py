#In this problem we have given a unique sorted array and we have to return the smallest sorted list 
#eg nums=[0,2,3,4,6,7]
#output=["0","2->4","6-7"]

from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not  nums:
            return res
        start=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                end=nums[i-1]
                if start==end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                start=nums[i]

        end=nums[-1]
        if start==end:
            res.append(str(start))
        else:
            res.append(f"{start}->{end}")
        return res
                

sol=Solution()
nums=[0,2,3,4,6,7]
res=sol.summaryRanges(nums)
print(res)
            
                
      

        