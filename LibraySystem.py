
class Item: 

    def __init__(self, title, author, year):
        self.title = title 
        self.author = author
        self.year = year 

    def display_info(self):
        print(f"{self.title} by {self.author} on year {self.year}")

class Book(Item):

    def __init__(self, title, author, year, genre, ISBN):
        super().__init__(self, title, author, year)
        self.genre = genre
        self.ISBN = ISBN 

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
        print(f"ISBN : {self.ISBN}")

class DVD(Item):

    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def display_info(self):
        super().display_info()

        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Duration: {self.duration}")

    