def leftposition(a,l,h,k):
    while (h-l>1):
        mid=int(l+(h-l)/2)
        if (a[mid]>=k):
            h=mid
        else:
            l=mid
    return h

def rightposition(a,l,h,k):
    while (h-l>1):
        mid=int(l+(h-l)/2)
        if (a[mid]<=k):
            l=mid
        else:
            h=mid
    return l

n=int(input())
a=[int(a) for a in input().split()]
k=int(input())
left=leftposition(a,-1,n-1,k)
right=rightposition(a,0,n,k)
if (a[left]==k and a[right]==k):
    print (right-left+1)
else:
    print (0)
