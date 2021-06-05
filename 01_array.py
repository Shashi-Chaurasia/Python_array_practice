# def Insert_number(item):
#     array = []
#     for i in item:
#         array = item
#         print(array)
# list = [5,6,8,2,5,7,8]
# Insert_number(list)

from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Current memory address and the length in elements of the buffer: "+str(array_num.buffer_info()))
# print("The size of the memory buffer in bytes: "+str(array_num.buffer_info()[1] * array_num.itemsize))
# for i in array_num:
#     print(i)

# print("First 3 array ")
# print(array_num[0])
# print(array_num[1])
# print(array_num[2])
