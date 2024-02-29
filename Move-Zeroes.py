def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
        print(nums)
moveZeroes([0,0,1])        