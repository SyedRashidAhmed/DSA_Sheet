class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                left_plot = (i==0) or (flowerbed[i-1]==0)
                right_plot = (i==len(flowerbed)-1) or (flowerbed[i+1]==0)
                if left_plot and right_plot:
                    flowerbed[i]=1
                    count+=1
        print(count>=n)   
    
obj=Solution().canPlaceFlowers([1,0,0,0,1],1)    