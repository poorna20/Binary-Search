def binary(a,l,h,k):
    while ((h-l)>1):
        
        mid=int(l+(h-l)/2)
        if (a[mid]<=k):
            l=mid
        else:
            h=mid
            
    return (a[l])


n=int(input())
a=[int(a) for a in input().split()]
k=int(input())
print (binary(a,0,n-1,k))
