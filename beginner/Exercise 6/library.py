class Library:                                                            
    def __init__(self):                         #init is a special method called automatically when an object is create, it sets up data for the object
                                                #Self refers to the current object and it allows the objects to store its own data
        self.books = []                         #a list to store the book names
        self.no_of_books = 0                    #an integer to keep counts of the books These objects are called instance variable 
    def add_book(self, book_name):              #method to add book to the library
        self.books.append(book_name)            #adds the book name to the list
        self.no_of_books += 1                   #increases the book count by 1, this keeps the list and count in sync
    def show_books(self):                       #this method show all the books present in the library
        print("Books in the Library: ")         #prints the heading
        for book in self.books:                 #loops goes through each book in the list
            print("-", book)                    #prints book names one by one 
    def get_no_of_books(self):                  #display the total number of books
        print("Total number of Books: ", self.no_of_books)                   #prints the count of the books

lib = Library()  #creating an object            #

#Adding books

lib.add_book("Ikigai")
lib.add_book("The Secret")
lib.add_book("The Half Girlfriend")
lib.add_book("The 101 Esaays")

#Display all the books
lib.show_books()

#display number of books
lib.get_no_of_books()
   

   #-----------HArry's Code---------------
#    class Library:
#     def __init__(self):
#         self.noBooks = 0
#         self.books = []
#     def addBook(self, book):
#         self.books.append(book)
#         self.noBooks = len(self.books)
#     def showInfo(self):
#         print(f"The Library has {self.noBooks} books. The books are")
#         for book in self.books:
#             print(book)
# l1 = Library()
# l1.addBook("Ikigai")
# l1.addBook("Ikigai")
# l1.addBook("Ikigai")
# l1.showInfo()












