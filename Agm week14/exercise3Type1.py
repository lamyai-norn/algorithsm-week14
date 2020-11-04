array2D=eval(input("value: "))
for n in range(len(array2D)):
    for i in range(len(array2D[n])):
        if array2D[n][i]==7:
           array2D[n][i]=8
print(array2D)