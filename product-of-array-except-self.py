class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result,cur=[],1
        start=0
        end=len(nums)-1
        for i in range(len(nums)):
            if start==end:
                continue
            else:
                ref=end
                while start<end:
                    cur=nums[end]*cur
                    end-=1
                end=ref-1    
            result.append(cur)
        print(result)
sol=Solution()
sol.productExceptSelf([1,2,3,4])    