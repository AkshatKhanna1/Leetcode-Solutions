# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        value1,value2,count1,count2 = None, None,0,0
        n=int(len(nums)/3)        

        for i in nums:
            if i==value1:
                count1+=1
            elif i==value2:
                count2+=1
            elif count1==0:
                count1,value1=1,i
            elif count2==0:
                count2,value2=1,i
            else:
                count1,count2=count1-1,count2-1

        itr1,itr2 = 0,0

        for i in nums:
            if i==value1:
                itr1+=1
            elif i==value2:
                itr2+=1

        array=[]

        if itr1>n:
            array.append(value1)
        if itr2>n:
            array.append(value2)  

        return array
