# from array import*

# list = [2,4,6,8,3,5]

# arr = array('i' , [])

# arr.fromlist(list)

# print(str(arr))

# from array import *
# array_num = array('i', [1, 3, 5, 7, 9])
# print("Original array: "+str(array_num))
# print("Insert new value 4 before 3:")

# array_num.pop(2)
# print("New array: "+str(array_num))

def dublicate_number(nums):
    new_list = set()
    dubilacet_no = -1

    for i in range(len(nums)):
        if nums[i] in new_list:
            return nums[i]
        else:
            new_list.add(nums[i])

    return dubilacet_no


print(dublicate_number([1,2,3,4,5,6,7,4]))
print(dublicate_number([1,2,3,4,5,6,7]))
print(dublicate_number([1,1,2,3,4,5,6,7,4]))
    








    




