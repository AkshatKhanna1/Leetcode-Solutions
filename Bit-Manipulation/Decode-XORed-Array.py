class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        k=first
        lst=[first]
        for i in encoded:
            k=k^i
            lst.append(k)
        return lst
        
