def findDublicate(arr):
   new_arr = set(arr)
   if arr != new_arr:
       print(new_arr)



nums = [1 ,3, 5, 1, 3, 7, 9]
findDublicate(nums)