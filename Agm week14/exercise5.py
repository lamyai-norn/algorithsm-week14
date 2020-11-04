array=eval(input("value:"))
list=[]
for n in range(len(array[0])):
    columnSum=0
    for i in range(0,len(array)):
        columnSum=columnSum+array[i][n]
    list.append(columnSum)
print(columnSum)