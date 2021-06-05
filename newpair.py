def maxProducts(arr):
    if(len(arr) < 2):
        return False

    x = arr[0]
    y = arr[1]

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j] > x*y:
                x=arr[i]
                y=arr[j]

    return x , y

num= [1,2,3,4,5,6,7]
print(num)
print("pair :" ,maxProducts(num))
