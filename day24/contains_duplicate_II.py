#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic={}
        for i,number in enumerate(nums):
            if number in dic:
                if i-dic[number]<=k:
                    return True

            dic[number]=i
        return False
                
           
            
                
        
        
s=Solution()
res=s.containsNearbyDuplicate([1,0,1,1],1)
print(res)