# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        sum=arr[0]
        for i in range(1,n):
            sum+=arr[i]
            arr[i]=sum
            
        if n<=2:
            return sum
        
        for i in range(2,n,2):
            left=-1
            right=i
            
            while right!=n:
                if left==-1:
                    sum+=arr[right]
                    left+=1
                    right+=1
                else:
                    sum+=arr[right]-arr[left]
                    left+=1
                    right+=1
        return sum
