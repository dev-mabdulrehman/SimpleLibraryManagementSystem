import os,json,datetime

class LibraryManagementSystem:
    def __init__(self):
        try:
            self.readJson("record")
        except:
            self.initialize()
    def initialize(self):
        data = {"books":[],"members":[],"booksIssued":[]}
        self.writeJson("record",data)
    def displayMenu(self):
        menu_list = [("1","Add New Book"),("2", "List of All Books"),
        ("3","Add New Member"),("4","List of All Members"),
        ("5","Issue a Book"),("6","Return a Book"),
        ("7","List of Issued Books"),("8","Exit")]
        print("Welcome to Library Management System\nPress:")
        for menu_item in menu_list:
            print(f"\t{menu_item[0]}. {menu_item[1]}")
    def performAction(self,choice):
        if choice == "1":
            self.addBook()
        elif choice == "2":
            self.listOfBook()
        elif choice == "3":
            self.addMember()
        elif choice == "4":
            self.listOfMember()
        elif choice == "5":
            self.issueBook()
        elif choice == "6":
            self.returnBook()
        elif choice == "7":
            self.listOfIssuedBooks()
        elif choice == "8":
            exit(1)
        else:
            return -1
    def writeJson(self,filename,data):
        with open(f"{filename}.json","w") as file:
            json.dump(data,file)
    def readJson(self,filename):
        with open(f"{filename}.json","r") as file:
            data = json.load(file)
        return data
    def addBook(self):
        print("Add Book")
        print("========\n")
        name = input("Book Name:")
        author = input("Book Author Name:")
        year = input("Book Year:")
        received = input("No. of Books Received:")
        book = (name,author, year, received)
        data = self.readJson("record")
        data["books"].append(book)
        self.writeJson("record",data)
    def getBooks(self):
        data = self.readJson("record")["books"]
        for index,book in enumerate(data):
            print(f"Book Index:{index+1}")
            print(f"Book Name:{book[0]}")
            print(f"Book Author:{book[1]}")
            print(f"Book Year:{book[2]}")
            print(f"Book Received:{book[3]}")
            print()
        return data
    def listOfBook(self):
        print("All Books")
        print("=========")
        data = self.getBooks()
        if len(data) != 0:
            print("EDIT(E)\nDELETE(D)")
            choice = input()
            if choice == "e" or choice == "E":
                index = int(input("Book Index:"))
                self.editBook(index)
            elif choice == "d" or choice == "D":
                index = int(input("Book Index:"))
                self.deleteBook(index)
    def editBook(self,index):
        data = self.readJson("record")
        books = data["books"]
        book = books[index-1]
        choice = input("What you want to Edit?\nName(N),Author Name(A),Year(Y),Received Books(R):")
        if choice == "N" or choice == "n":
            name = input("Book Name:")
            book[0] = name
        elif choice == "A" or choice == "a":
            author = input("Book Author Name:")
            book[1] = author
        elif choice == "Y" or choice == "y":
            year = input("Book Year:")
            book[2] = year
        elif choice == "R" or choice == "r":
            received = input("No. of Books Received:")
            book[3] = received
        else:
            print("Invalid Choice")
            return
        books[index-1] = book
        data["books"] = books
        self.writeJson("record",data)
        print("Edited Successfully")
    def deleteBook(self,index):
        data = self.readJson("record")
        books = data["books"]
        del books[index-1]
        self.writeJson("record",data)
    def addMember(self):
        print("Add Member")
        print("========\n")
        name = input("Member Name:")
        cnic = input("CNIC:")
        dob = input("DOB:")
        member = (name,cnic, dob)
        data = self.readJson("record")
        data["members"].append(member)
        self.writeJson("record",data)
    def getMembers(self):
        data = self.readJson("record")["members"]
        for index,member in enumerate(data):
            print(f"Member Index:{index+1}")
            print(f"Name:{member[0]}")
            print(f"CNIC:{member[1]}")
            print(f"DOB:{member[2]}")
            print()
        return data
    def listOfMember(self):
        print("All Member")
        print("=========")
        data = self.getMembers()
        if len(data) != 0:
            print("EDIT(E)\nDELETE(D)")
            choice = input()
            if choice == "e" or choice == "E":
                index = int(input("Member Index:"))
                self.editMember(index)
            elif choice == "d" or choice == "D":
                index = int(input("Member Index:"))
                self.deleteMember(index)
    def editMember(self,index):
        data = self.readJson("record")
        members = data["members"]
        member = members[index-1]
        choice = input("What you want to Edit?\nName(N),CNIC(C),DOB(D):")
        if choice == "N" or choice == "n":
            name = input("Member Name:")
            member[0] = name
        elif choice == "C" or choice == "c":
            cnic = input("CNIC:")
            member[1] = cnic
        elif choice == "D" or choice == "d":
            dob = input("DOB:")
            member[2] = dob
        else:
            print("Invalid Choice")
            return
        member[index-1] = member
        data["members"] = member
        self.writeJson("record",data)
        print("Edited Successfully")
    def deleteMember(self,index):
        data = self.readJson("record")
        members = data["members"]
        del members[index-1]
        print("Deleted Successfully")
        self.writeJson("record",data)
    def issueBook(self):
        print("All Books")
        print("=========")
        self.getBooks()
        bookIndex = int(input("Book Index:"))-1
        books = self.readJson("record")["books"]
        bookName = books[bookIndex][0]
        print()
        print("All Members")
        print("===========")
        self.getMembers()
        memberIndex = int(input("Member Index:"))-1
        members = self.readJson("record")["members"]
        memberName = members[memberIndex][0]
        dateTime = datetime.datetime.now()
        dateTime = dateTime.strftime("%d-%m-%Y")
        issueBook = (bookName, memberName, dateTime, "00-00-0000")
        data = self.readJson("record")
        data["booksIssued"].append(issueBook)
        self.writeJson("record",data)
        print("Successfully Issued Book")
    def getIssuedBooks(self):
        issuedBooks = self.readJson("record")["booksIssued"]
        for index,issuedBook in enumerate(issuedBooks):
            if issuedBook[-1] == "00-00-0000":
                print(f"Index:{index+1}")
                print(f"Book Name:{issuedBook[0]}")
                print(f"Member Name:{issuedBook[1]}")
                print(f"Issued Date:{issuedBook[2]}")
    def returnBook(self):
        print("Issued Books")
        print("============\n")
        self.getIssuedBooks()
        index = int(input("Index:"))-1
        data = self.readJson("record")
        booksIssued = data["booksIssued"]
        dateTime = datetime.datetime.now().strftime("%d-%m-%Y")
        booksIssued[index][-1] = dateTime
        self.writeJson("record",data)
    def listOfIssuedBooks(self):
        print("All Issued Books")
        print("================")
        self.getIssuedBooks()
        input()

if __name__ == "__main__":
    while True:
        os.system('cls')
        obj = LibraryManagementSystem()
        obj.displayMenu()
        choice = input()
        os.system('cls')
        response = obj.performAction(choice)
        if response == -1:
            print("Invalid Choice")

