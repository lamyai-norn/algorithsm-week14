persons=eval(input("persons: "))
age=int(input("age:"))
for value in persons:
   if value[2]==age:
       print(value[0])