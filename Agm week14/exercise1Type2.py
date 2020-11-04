def isEqual(list1,list2):
    if len(list1)!=len(list2):
        return False
    else:
        for n in range(len(list1)):
            if list1[n]!=list2[n]:
                return False
        return True
list1=eval(input("value1:"))
list2=eval(input("value2:"))
if isEqual(list1,list2):
    print("EQUAL")
else:
    print("NOT EQUAL")