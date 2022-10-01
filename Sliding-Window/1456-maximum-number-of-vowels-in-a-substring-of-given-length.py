# O(N) Time Complexity
# O(1) Space Complexity

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a","e","i","o","u"}
        n=len(s)
        countVowel=0
        for i in range(k):
            if s[i] in vowels:
                countVowel+=1
        maxVowelCount=countVowel
        for i in range(k,n):
            print(countVowel)
            if maxVowelCount==k:
                return k
            if s[i-k] in vowels:
                countVowel-=1
            if s[i] in vowels:
                countVowel+=1
            if countVowel>maxVowelCount:
                maxVowelCount=countVowel
            
        return maxVowelCount
