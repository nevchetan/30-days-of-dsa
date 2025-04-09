#In this problem there are two strings provided and you have to merge them alternately

class Solution:
    def MergeAlternately(self, word1 :str,word2: str)->str:
        res=[]
        word_f=list(word1)
        word_s=list(word2)

        for i in range(min(len(word_f),len(word_s))):
            res.append(word_f[i])
            res.append(word_s[i])

        if len(word_f)<len(word_s):
            res.extend(word_s[len(word_f):])
        else:
            res.extend(word_f[len(word_s):])

        
        return ''.join(res)

s=Solution()
word1="abcd"
word2="pq"

ans=s.MergeAlternately(word1,word2)
print(ans)