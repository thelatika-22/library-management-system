#DATABASE
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


class Book:
    def __init__(self, title):
        self.title = title
        self.status = "Available"


class Library:
    def __init__(self):
        self.books = {}
        self.issued_books = {}

    # ADD BOOK
    def add_books(self):
        title = input("Enter Book Name: ").title()

        if title not in self.books and title not in self.issued_books:
            self.books[title] = Book(title)
            print(title, "added successfully.")
        else:
            print("Book already exists.")

    # AVAILABLE BOOKS
    def available_books(self):
        if not self.books:
            print("NO BOOKS AVAILABLE")
        else:
            print("\nBOOKS AVAILABLE:")
            for book in self.books:
                print(book)

    # SEARCH BOOK
    def search_book(self):
        keyword = input("Enter book name to search: ").lower()

        result = list(
            filter(
                lambda x: keyword in x.lower(),
                self.books.keys()
            )
        )

        if result:
            print("\nMatching Books:")
            for book in result:
                print(book)
        else:
            print("Book not found.")

    # ISSUE BOOK
    def issue_book(self):
        title = input("Enter the book you want to issue: ").title()

        if title in self.books:

            name = input("Enter Student Name: ").title()

            try:
                roll = int(input("Enter Roll Number: "))
                issue_day = int(input("Enter Issue Day: "))
            except ValueError:
                print("Please enter numeric values only.")
                return

            student = Student(name, roll)

            self.issued_books[title] = {
                "Student": student,
                "Issue_day": issue_day
            }

            del self.books[title]

            print(title, "issued successfully.")

        else:
            print("Book not available.")

    # RETURN BOOK
    def return_book(self):
        title = input("Enter the book you want to return: ").title()

        if title in self.issued_books:

            data = self.issued_books[title]

            try:
                return_day = int(input("Enter Return Day: "))
            except ValueError:
                print("Please enter numeric values only.")
                return

            if return_day < data["Issue_day"]:
                print("Invalid return day.")
                return

            days = return_day - data["Issue_day"]

            calculate_fine = lambda d: (d - 7) * 5 if d > 7 else 0
            fine = calculate_fine(days)

            student = data["Student"]

            print("\nBook Returned Successfully")
            print("Student:", student.name)
            print("Roll Number:", student.roll)
            print("Days Kept:", days)
            print("Fine: Rs", fine)

            self.books[title] = Book(title)

            del self.issued_books[title]

        else:
            print("Book not found in issued records.")

    # STUDENT NAMES
    def students_name(self):

        if not self.issued_books:
            print("No books are currently issued.")
            return

        names = list(
            {
                data["Student"].name
                for data in self.issued_books.values()
            }
        )

        print("Students who issued books:")
        for name in names:
            print(name)

    # BOOKS BY LETTER
    def books_by_letter(self):
        letter = input("Enter starting letter: ").upper()

        result = list(
            filter(
                lambda x: x.upper().startswith(letter),
                self.books.keys()
            )
        )

        if result:
            print("Matching Books:")
            for book in result:
                print(book)
        else:
            print("No books found.")

    # BOOK -> ROLL NUMBER DICTIONARY
    def roll_numbers(self):

        if not self.issued_books:
            print("No books are currently issued.")
            return

        rolls = {
            book: data["Student"].roll
            for book, data in self.issued_books.items()
        }

        print("\nBook -> Roll Number")
        print(rolls)

    # MENU
    def menu(self):

        while True:

            print("\n========== LIBRARY MENU ==========")
            print("1. ADD BOOK")
            print("2. AVAILABLE BOOKS")
            print("3. SEARCH BOOK")
            print("4. ISSUE BOOK")
            print("5. RETURN BOOK")
            print("6. STUDENT NAMES")
            print("7. BOOKS STARTING WITH LETTER")
            print("8. ROLL NUMBERS DICTIONARY")
            print("9. EXIT")

            try:
                choice = int(input("\nEnter Your Choice: "))

                if choice == 1:
                    self.add_books()

                elif choice == 2:
                    self.available_books()

                elif choice == 3:
                    self.search_book()

                elif choice == 4:
                    self.issue_book()

                elif choice == 5:
                    self.return_book()

                elif choice == 6:
                    self.students_name()

                elif choice == 7:
                    self.books_by_letter()

                elif choice == 8:
                    self.roll_numbers()

                elif choice == 9:
                    print("Thank You!")
                    break

                else:
                    print("INVALID CHOICE")

            except ValueError:
                print("Please enter numbers only.")


obj = Library()
obj.menu()

