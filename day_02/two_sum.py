# given a array=[2,7,11,15] and a target =9 and the output should be list of index [0,1]
class solution:
    def two_sum(self,nums:list[int],target:int)->list[int]:
        hashmap={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i


s=solution()

array=[2,7,5,11,15]
target=9

result=s.two_sum(array,target)
print("output:", result)