
class Item:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"{self.title} by {self.author} ({self.year})")

# Now class Book is a Item Is a -> Inheritance  
# Parent, initializes our own fields 
class Book(Item):

    def __init__(self, title, author, year, genre, isbn):
        super().__init__(title, author, year)

        self.genre = genre
        self.isbn = isbn 

    def display_info(self):

        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
        print(f"ISBN: {self.isbn}")

class DVD(Item):

    # calling super.__int__() -> the optimization examination wants to seee 
    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    # We are extending the parent class Item 
    # But here we are overirding this funtion as per need 
    def display_info(self):

        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Duration: {self.duration} minutes")
