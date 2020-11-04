def isEqual(list1,list2):
    if len(list1)==len(list2):
        count=0
        for n in range(len(list1)):
            if list1[n]==list2[n]:
                count+=1
        if count==len(list1):
            return True
        else:
            return False
    return False
list1=eval(input("values1:"))
list2=eval(input("values2:"))
if isEqual(list1,list2):
    print("EQUAL")
else:
    print("NOT EQUAL")
