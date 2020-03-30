def binary(a,l,h,k):
    while (l<=h):
        mid=int(h+l/2)
        if (a[mid]==k):
            return mid
        elif (a[mid]<k):
            l=mid+1
        else:
            h=mid-1
    return (-1)
n=int(input())
a=[int(a) for a in input().split()]
k=int(input())
print (binary(a,0,n-1,k))
