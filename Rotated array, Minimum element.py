def rotated(a,l,h):
    if (a[l]<=a[h]):
        return l
    while (l<=h):
        if (l==h):
            return l
        mid=int(l+(h-l)/2)
        if (a[mid]<a[h]):
            h=mid
        else:
            l=mid+1
    return -1

n=int(input())
a=[int(a) for a in input().split()]
print (rotated(a,0,n-1))

