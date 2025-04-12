#to check the longest prefix for given list of strings (https://leetcode.com/problems/longest-common-prefix/)
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # Initialize the prefix with the first string

        for string in strs[1:]:  # Loop through all the other strings
            # While the current string does not start with the prefix
            while not string.startswith(prefix):
                # Shorten the prefix by one character at a time
                prefix = prefix[:-1]
                
                # If prefix becomes empty, return an empty string (no common prefix)
                if not prefix:
                    return ""
        
        return prefix  # Return the longest common prefix
sol=Solution()
strs=["flower","flow","flight"]
res=sol.longestCommonPrefix(strs)
print(res)