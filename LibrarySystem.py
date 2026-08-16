class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title 
        self.author = author 
        self.available = True  # State changes when borrowed / returned 

    def display_info(self):
        status = "Available" if self.available else "Borrowed"; 
        print(f"{self.book_id} - {self.title} by {self.author} [{status}]")

class Member:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
        self.borrowed_books = []

class Library:
    pass