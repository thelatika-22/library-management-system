#DATABASE
student_data={}
books={}
issued_books={}

#ADD BOOK FUNCTION
def add_books():
    book_name=input("\nEnter the Book Name:")
    books[book_name]="available"
    print(book_name,"is Successfully Added")

#AVAILABLE BOOKS FUNCTION
def available_books():
    if len(books)==0:
        print("NO BOOKS AVAILABLE")
    else:
        print("BOOKS AVAILABLE:")
        for book in books:
            print(book)

#ISSUE BOOK FUNCTION
def issue_book():
    if len(books)==0:
        print("No Books Available")
        return
    
    book_name=input("\nEnter the Book You Want To Issue:") 
    if book_name in books:
        name=input("Enter your Name:")
        roll=int(input("Enter your roll number:"))
        issue_day=int(input("Enter Issue day:"))

        issued_books[book_name]={"name":name,"roll":roll,"issue_day":issue_day}

        del books[book_name]
        print(book_name,"is Issued")
    else:
        print(book_name,"is Not Available")

#RETURN BOOK FUNCTION
def return_book():
    book_name=input("Enter the Book You Want to Return:")
    if book_name in issued_books:
        data=issued_books[book_name]

        issue_day=data["issue_day"]
        return_day=int(input("Enter return date(in days):"))
        days=return_day-issue_day
        fine=0
        print("\nBook Returned Successfully")
        print("Student:",data["name"])
        print("Roll No:",data["roll"])
        print("Days:",days)
        if days>7:
            fine=(days-7)*5
            print("Fine:Rs",fine)
        else:
            print("Returned on time.No fine!") 
        books[book_name]="available"
        del issued_books[book_name]

        print(book_name,"Is Returned Successfully")
    else:
        print(book_name,"Not Found")

#MAIN BODY
def library():
    while True:
        print("\nMENU")
        print("1.ADD BOOKS")
        print("2.AVAILABLE BOOKS")
        print("3.ISSUE BOOK")
        print("4.RETURN BOOK")
        print("5.EXIT")

        choice =int(input("ENTER YOUR CHOICE:"))

        if choice==1:
            add_books()
        elif choice==2:
            available_books()
        elif choice==3:
            issue_book()
        elif choice==4:
            return_book()
        elif choice==5:
            print("THANK YOU!")
            break
        else:
            print("INVALID CHOICE")
            break

library()

