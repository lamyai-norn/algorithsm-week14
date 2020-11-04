def splitBySpace(theString):
    list=[]
    string=""
    for n in range(len(theString)):
        if theString[n]!=" ":
            string+=theString[n]
        else:
            list.append(string)
            string=""
    list.append(string)
    return list
word=input("word: ")
print(splitBySpace(word))