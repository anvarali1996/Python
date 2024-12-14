# MAGIC METHODS
search = input("Search book: ")
# add_book = input("Add book (format: title,author,num_pages): ")

class Book:
    def __init__(self, title, author, num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other) -> str:
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

    
book1 = Book("The Hoblit", "J.R.R. Tolkien", 170)
book4 = Book("The Hoblit", "J.R.R. Tolkien", 170)
book2 = Book("Harry Potter and the Philosopher's stone", "J.K. Rowling", 320)
book3 = Book("The lion, the witch and the Wardrobe", "C.S. Lewis", 172)
books = [book1, book2, book3, book4]
# print(book4.title)
# print(book1 == book4)
# print(book1 < book3)
# print(book3 + book1)
# print("lion" in book3)
# print(search in book1)
# print(book4['title'])
print(book3['num_pages'])


# Search for the book
print("\nSearch Results:")
for book in books:
    if search in book:
        print(book)

# Adding new book
# if add_book:
#     try:
#         title, author, num_pages = add_book.split(",")
#         num_pages = int(num_pages.strip())  
#         new_book = Book(title.strip(), author.strip(), num_pages)

#         # Assign dynamic variable name for the new book (book4, book5, etc.)
#         book_var_name = f"book{len(books) + 1}"
#         globals()[book_var_name] = new_book  
#         books.append(new_book)  

#         print(f"\nAdded new book: {new_book}")
#     except ValueError:
#         print("\nInvalid format. Please use the format: title,author,num_pages")

# Print all books
print("\nAll Books:")
for book in books:
    print(book)
