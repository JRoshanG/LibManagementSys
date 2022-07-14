from datetime import datetime
import os

# Function to Read TextFile BookDetails
def readTxtFile():
    file = open("BookDetails.txt","r")
    i = 1
    for line in file:
        line = line.replace("\n","")
        bookDetailDict[i] = line.split(",")
        i = i + 1
    return bookDetailDict
    file.close()   

# Function to Print Complete Details In GUI
def printBookDetailDict():
    print("---------------------------------------------------------------------------------------------")
    print("{:<12} {:<32} {:<25} {:<15} {:<15}".format('Book ID','Book Name','Author','Quantity','Price'))
    print("---------------------------------------------------------------------------------------------")
    file = open("BookDetails.txt","r")
    i = 1
    for line in file:
        line = line.replace("\n","")
        line = line.split(",")
        bookID = i
        bookName = line[0]
        author = line[1]
        quantity = line[2]
        price = line [3]
        i = i + 1
        print("{:<12} {:<32} {:<25} {:<15} {:<15}".format(bookID, bookName, author, quantity, price))
    print("---------------------------------------------------------------------------------------------\n")
    file.close()

# Function to Call for Try Catch Error
def tryCatchError():
    print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("             Please Proveide Valid Input Only")
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Function that Ask User for Input 1,2,3
def userInput():
    check = "notTrue"
    while check != "True":
        print ("Enter '1' to borrow a book")
        print ("Enter '2' to retrun a book")
        print ("Enter '3' to Exit")
        try:
            ansNum = int(input("Please Enter a Value: "))
            check = "True"
        except:
            tryCatchError()
    return ansNum

# Function to Check if User Input is 1,2 or 3
def checkUserInput(ansNum):
    if ansNum == 1:
        bookID = checkBookID(ansNum)
        available = borrowBook(bookID)
        if available == "true":
            userNameBorrow(bookID, ansNum)
    elif ansNum == 2:
        bookID = checkBookID(ansNum)
        returnBook()
        userNameReturn(bookID, ansNum)
    elif ansNum == 3:
        exit
    else :
        invalidInput()

#Call Function when User Input 1
def borrowBook(bookID):
    dictValue = bookDetailDict[bookID]
    bookQuantity = int(dictValue[2])
    if bookQuantity == 0:
        print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                Book is Not Available")
        print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        available = "false"
    else:            
        print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                Book is Available")
        print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        available = "true"
    return available


#To check User Input For BookID
def checkBookID(ansNum):
    if ansNum == 1:
        check = "notTrue"
        while check != "True":
            try:
                bookID = int(input("\nEnter the ID of Book you want to Borrow: "))
                check = "True"
            except:
                tryCatchError()
    elif ansNum == 2:
        check = "notTrue"
        while check != "True":
            try:
                bookID = int(input("\nEnter the ID of Book you want to Return: "))
                check = "True"
            except:
                tryCatchError()

    while bookID <= 0 or bookID > (len(bookDetailDict)):
        print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("            Please Provide Valid Book ID")
        print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        printBookDetailDict()
        if ansNum == 1:
            bookID = int(input("\nEnter the ID of Book you want to Borrow: "))
        elif ansNum == 2:
            bookID = int(input("\nEnter the ID of Book you want to Return: "))
    return bookID

#Function to Ask Name of User and Display Price and Time
def userNameBorrow(bookID, ansNum):
    nameOfUser = input("Enter the Name of Person who borrowed book: ")
    dictValue = bookDetailDict[bookID]
    bookPrice = dictValue[3]
    dateTime = datetime.now()
    dt_string = dateTime.strftime("%Y/%m/%d %H:%M:%S")
    print("The Price of Book is", bookPrice)
    print("Date and Time of borrow is",dt_string)
    updateTxtFile(bookID, ansNum)
    borrowAnother("y", nameOfUser, dt_string, bookPrice, bookID, ansNum)

#Function to Ask Name of User to Return the Name
def userNameReturn(bookID, ansNum):
    nameOfUser = input("Enter the Name of Person who returned the book: ")
    calculateFine = bookFine(0)
    dictValue = bookDetailDict[bookID]
    dateTime = datetime.now()
    dt_string = dateTime.strftime("%Y/%m/%d %H:%M:%S")
    print("Date and Time of Return is",dt_string)
    updateTxtFile(bookID, ansNum)
    returnAnother("y", nameOfUser, dt_string, bookID, calculateFine, ansNum)

# Function to Ask for Borrow Another Book 
def borrowAnother(borrowedAnother, customerName, dateTime, bookPrice, bookID, ansNum):
    totalPrice = 0
    booksBorrowed = []
    booksBorrowed.append(bookID)
    while borrowedAnother == "y" or borrowedAnother == "Y":
        totalPrice = totalPrice + convertBookPrice(bookPrice)
        printBookDetailDict()
        print("Have this person borrowed another book as well ?")
        borrowedAnother = input("if 'Yes' please enter 'y' or else provide any other value: ")
        if borrowedAnother == "y" or borrowedAnother == "Y":
            bookID = checkBookID(ansNum)
            isAvailable = borrowBook(bookID)
            if isAvailable == "true":
                dictValue = bookDetailDict [bookID]
                bookPrice = dictValue[3]
                booksBorrowed.append(bookID)
                print("The Price of Book is", bookPrice)
                updateTxtFile(bookID, ansNum)
    customerBorrowDetail(customerName, totalPrice, dateTime, booksBorrowed)
    billingBorrowCustomerDetail(customerName, totalPrice, dateTime, booksBorrowed)

# Function to Calculate Days of Return
def bookFine(totalFine):
    check = "notTrue"
    while check != "True":
        try:
            days = int(input("How many Days after has this Book been Returned: "))
            check = "True"
        except:
            tryCatchError()
    if days > 10:
        totalDay = days - 10
        fine = totalDay * 1
        totalFine = totalFine + fine
    return totalFine

# Function to Ask for Return Another Book
def returnAnother(returnedAnother, customerName, dateTime, bookID, calculateFine, ansNum):
    booksReturned = []
    booksReturned.append(bookID)
    while returnedAnother == "y" or returnAnother == "Y":
        printBookDetailDict()
        print("Have this person returned another book as well ?")
        returnedAnother = input("if 'Yes' please enter 'y' or else provide any other value: ")
        if returnedAnother == "y" or returnedAnother == "Y":
            bookID = checkBookID(ansNum)
            dictValue = bookDetailDict [bookID]
            booksReturned.append(bookID)
            calculateFine = bookFine(calculateFine)
            updateTxtFile(bookID, ansNum)
    customerReturnDetail(customerName, dateTime, booksReturned, calculateFine)
    billingReturnCustomerDetail(customerName, dateTime, booksReturned, calculateFine)

# Function to Update Quantity
def updateQuantity(bookID, ansNum):
    dictValue = bookDetailDict[bookID]
    if ansNum == 1:
        dictValue[2] = str(int(dictValue[2])-1)
    elif ansNum == 2:
        dictValue[2] = str(int(dictValue[2])+1)

# Function to Change and Write Quantity in Text
def updateTxtFile(bookID, ansNum):
    updateQuantity(bookID, ansNum)
    tempFile = open("TempBookDetailsDict.txt","w")
    i = 1
    while (i <= len(bookDetailDict)):
        bookDetail = bookDetailDict[i]
        tempFile.write(str(bookDetail)+"\n")
        i = i + 1
    tempFile.close()

    fileRead = open("TempBookDetailsDict.txt","r")
    fileWrite = open("TempBookDetail.txt","w")
    for line in fileRead:
        line = line.replace("[","")
        line = line.replace("]","")
        line = line.replace("'","")
        line = line.replace("  "," ")
        fileWrite.write(str(line))
    fileRead.close()
    fileWrite.close()
    os.remove("TempBookDetailsDict.txt")
    os.remove("BookDetails.txt")
    os.rename(r'TempBookDetail.txt',r'BookDetails.txt')
 
#Function to Convert Book price to Float
def convertBookPrice(bookPrice):
    price = bookPrice.replace("$","")
    price = float(price)
    return price

#Function to Print Customer Borrow Details
def customerBorrowDetail(customerName, totalPrice, dateTime, booksBorrowed):
    print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("            Customer Borrow Details")
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    
    print("Name of Customer:", customerName)
    print("Total Price from Borrow:","$"+ str(totalPrice))
    print("Date and Time of Borrow:",dateTime)
    print("\nBooks Borrowed are:")
    for books in booksBorrowed:
        dictValue = bookDetailDict [books]
        bookName = dictValue [0]
        print(bookName)
    print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Function to Print Customer Return Details
def customerReturnDetail(customerName, dateTime, booksReturned, totalPrice):
    print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("            Customer Return Details")
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    print("Name of Customer:", customerName)
    print("Date and Time of Return:",dateTime)
    if totalPrice != 0:
        print("Late Fine for Book is $"+str(totalPrice))
    print("\nBooks Returned are:")
    for books in booksReturned:
        dictValue = bookDetailDict [books]
        bookName = dictValue [0]
        print(bookName)
    print ("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Function to Create Bill Detail of Customer
def billingBorrowCustomerDetail(customerName, totalPrice, dateTime, booksBorrowed):
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    hour = str(datetime.now().hour)
    minute = str(datetime.now().minute)
    second = str(datetime.now().second)
    time = year + month + day + hour + minute + second 
    billCustomer = open(customerName + " " + time + ".txt","w")
    billCustomer.write("Name of Customer: " + customerName + "\n")
    billCustomer.write("Total Price for Borrow: " + "$" + str(totalPrice) + "\n")
    billCustomer.write("Date and Time of Borrow: "+ dateTime + "\n")
    billCustomer.write("Books Borrowed are:"+ "\n")
    for books in booksBorrowed:
        dictValue = bookDetailDict [books]
        bookName = dictValue [0]
        billCustomer.write (bookName + "\n")

# Function to Create Return Bill Detail of Customer
def billingReturnCustomerDetail(customerName, dateTime, booksReturned, totalPrice):
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    hour = str(datetime.now().hour)
    minute = str(datetime.now().minute)
    second = str(datetime.now().second)
    time = year + month + day + hour + minute + second 
    billCustomer = open(customerName + " " + time + ".txt","w")
    billCustomer.write("Name of Customer: " + customerName + "\n")
    billCustomer.write("Date and Time of Return: "+ dateTime + "\n")
    if totalPrice == 0:
        billCustomer.write("There is No Late Fee\n")
    elif totalPrice != 0:
        billCustomer.write("The Late fee for Book is $"+str(totalPrice)+"\n")
    billCustomer.write("Books Returned are:"+ "\n")
    for books in booksReturned:
        dictValue = bookDetailDict [books]
        bookName = dictValue [0]
        billCustomer.write (bookName + "\n")

#Call Function when User Input 2
def returnBook():
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("              You will now Return the Book")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


# Function to Call when user Input is Invalid 
def invalidInput():
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                      Ivalid Input!!!")
    print("             Please provide value as 1, 2 or 3.")    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

bookDetailDict = {}
bookDetailDict = readTxtFile()
