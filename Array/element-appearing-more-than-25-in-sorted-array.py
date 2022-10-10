# O(N) Time Complexity
# O(1) Space Complexity
# It was already mentioned in question that there is always 1 element which occur more than 25% times.

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        element=arr[0]
        count=1
        for i in arr[1:]:
            if count>n//4:
                break
            if element==i:
                count+=1
            else:
                element=i
                count=1
        return element
