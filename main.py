class Library:
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            book_info = line.split(',')
            book_name = book_info[0]
            author = book_info[1]
            print(f"Book: {book_name}, Author: {author}")

    def add_book(self):
        book_title = input("Enter book title: ")
        author = input("Enter author: ")
        release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")
        
        book_info = f"{book_title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")
        
    def remove_book(self, book_title):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        books_list = []

        for line in lines:
            if book_title.lower() not in line.lower():
                books_list.append(line)

        self.file.seek(0)
        self.file.truncate()
        
        for book in books_list:
            self.file.write(book + '\n')

        print(f"Book '{book_title}' removed successfully.")


lib = Library("books.txt")

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        print("\n")
        lib.list_books()
    elif choice == "2":
        print("\n")
        lib.add_book()
    elif choice == "3":
        print("\n")
        book_title = input("Enter the title of the book to remove: ")
        lib.remove_book(book_title)
    elif choice == "q":
        print("\n")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")