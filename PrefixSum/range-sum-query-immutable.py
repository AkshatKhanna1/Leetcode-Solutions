# O(1) Time Complexity
# O(1) Space Complexity

# In this solution, we have to do some pre-processing after that all opertions takes constant time.
# Pre-Processing takes O(N) Time Complexity


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=self.prefixSum(nums)
    
    def prefixSum(self, array):
        val=array[0]
        for i in range(1,len(array)):
            array[i]+=val
            val=array[i]
        return array

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.nums[right]
        return self.nums[right]-self.nums[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
