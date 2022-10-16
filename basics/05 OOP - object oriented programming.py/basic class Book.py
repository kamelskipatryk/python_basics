
class Book:
    def __init__(self, author, title = 'unknown', isbn = 'unknown', year = 'unknown'):
        self.author = author
        self.title = title
        self.isbn = isbn
        self.year = year

    def print_data(self):
        print( self.author, self.title, self.isbn, self.year )

book_1 = Book('Olka Kowalska', 'Podróże', '1245FDF6', 2022)
book_1.print_data()

book_2 = Book('Monia Pukowska', 'Samochody', year = 2015)
book_2.print_data()






