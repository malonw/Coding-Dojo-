arr=[5,9,6,7,3,2,1,8,4]
def Sort(arr):
    print("Oringinal:", arr)
    n= len(arr)
    for i in range(1,n):
        key=arr[i]
        v=i-1
        
        while v>=0 and key < arr[v]:
            arr[v+1]=arr[v]
            v -= 1
        
        arr[v+1]=key
    print("Sorted:",arr)
Sort(arr)