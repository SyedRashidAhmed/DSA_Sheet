def pivot(nums):
    lefts,rights=0,sum(nums)
    for i , x in enumerate(nums):
        rights-=x
        if lefts==rights:
            return i
        lefts+=x 
    return -1

pivot([1,2,3])