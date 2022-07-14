import functions

#Starting Execution Point
print ("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("          Hello and Welcome to Library Management System")
print ("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

ansNum = 0
# Creating a Loop for User until 3 is Inputed
if ansNum == 0:
    while ansNum != 3:
        functions.printBookDetailDict()
        ansNum = functions.userInput()
        functions.checkUserInput(ansNum)

print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("          Thank you for using out Lbirary Management System")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
