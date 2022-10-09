# O(log N) Time Complexity
# O(1) Space Complexity

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a|b==c:
            return 0
        flipCount=0
        while a>0 or b>0 or c>0:
            if (a|b)&1 != c&1:
                if c&1==1:
                    flipCount+=1
                else:
                    if a&1==1:
                        flipCount+=1
                    if b&1==1:
                        flipCount+=1
            a,b,c=a>>1,b>>1,c>>1
        return flipCount
