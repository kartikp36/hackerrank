number = int(input())

for lineNumber in range(1,number + 1):
    theString = ""
    for _ in range(number - lineNumber):
        theString += " "
    for _ in range(lineNumber):
        theString += "#"
    print(theString)