from array import*


d1 = [2,"shashi",6,8]
d2 = [2,7,9,8]
d3 = [9,4,3,]
d4 = [7,8,8]

arr = [[d1] , [d2] , [d3] , [d4]]

for i in arr:
    for c in i:
        print(c , end=" ")
    print()