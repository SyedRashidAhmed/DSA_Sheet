def rev(a):
    start=0
    end=len(a)-1
    while start < end :
        a[start],a[end]=a[end],a[start]
        start+=1
        end-=1
    print(*a)    
    # print(a[::-1])
    
        
if __name__=="__main__":
    a=list(map(int,input('enter the array\t').split()))
    rev(a)   
 