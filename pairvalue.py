def maxProdut(arr):
    arr_len = len(arr)

    #initalize the pair value
    x = arr[0] 
    y = arr[1]

    for i in range(0 , arr_len):
        for j in range(i+1 , arr_len):
            if (arr[i] * arr[j] > x *y):
                x = arr[i] 
                y = arr[j]

    return x , y 

nums = [1,2,3,4,5,6,7,8]
print("Number is : " , nums)
print("Pair value is : " , maxProdut(nums))

nums2 = [-1 ,-2 ,-3 , -4 , -5 , -6]
print("number two is :" , nums2)
print("pair value is : " , maxProdut(nums2))
     