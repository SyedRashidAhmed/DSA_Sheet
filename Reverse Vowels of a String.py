class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        word=list(s)
        vowels="aeiouAEIOU"
        start=0
        end=len(s)-1
        while start < end:
            while start < end and vowels.find(word[start]) == -1:
                start+=1
            while start < end and vowels.find(word[end]) == -1:
                end-=1
            word[start], word[end] = word[end], word[start]
            start+=1
            end-=1
        print("".join(word))
    
ob=Solution().reverseVowels('leetcode')    