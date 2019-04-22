from library import Book

class Novel(Book):
    def __init__(self, bookId=0, title = '', genre = '', price = 0, rating = 0):
        super().__init__(bookId, title, price, rating)
        self.genre = genre

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def __str__(self):
        return super().__str__() + f'Genre: {self.genre}'

    def __eq__(self,other):
        if not isinstance(other, Novel):
            return NotImplemented
        b = super().__eq__(other)
        return self.genre == other.genre and b

    def show(self):
        super().show()
        print(f'Genre: {self.genre}')

    def updateBook(self, book_id, book_title, book_price, book_rating, book_genre):
        self.bookId = book_id
        self.title = book_title
        self.price = book_price
        self.rating = book_rating
        self.genre = book_genre
