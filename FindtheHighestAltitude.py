def al(gain):
    gain.insert(0,0)
    for i in range(1,len(gain)):
        x=gain[i]+gain[i-1]
        gain.pop(i)
        gain.insert(i,x)
    print(gain)
    print(max(gain))


al([-5,1,5,0,-7])    