# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        sum=0
        n=len(arr)
        for i in range(k):
            sum+=arr[i]
        if sum>=threshold*k:
            count+=1
        for i in range(k,n):
            sum=sum+arr[i]-arr[i-k]
            if sum>=threshold*k:
                count+=1
        return count
