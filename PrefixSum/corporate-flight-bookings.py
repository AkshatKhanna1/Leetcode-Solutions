# O(MAX(N,K)) Time Complexity
# O(N) Space Complexity

def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        array=[0]*n
        for itr in bookings:
            array[itr[0]-1]+=itr[2]
            if itr[1]!=n:
                array[itr[1]]-=itr[2]
        prefixSum=0
        for i in range(n):
            prefixSum+=array[i]
            array[i]=prefixSum
        return array
