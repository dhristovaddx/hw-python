class Book:
    count = 0

    def __init__(self, bookId, title, author, price, rating):
      self.bookId = bookId
      self.title = title
      self.author = author
      self.price = price
      self.rating = rating
  
    books = []
    @property
    def bookId(self):
        return self._bookId

    @bookId.setter
    def bookId(self,bookId):
        assert bookId >= 0, 'bookId must be positive'
        self._bookId = bookId

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self,author):
        self._author = author

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,price):
        self._price = price

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self,rating):
        self._rating = rating
    
    def __str__(self):
        '''str(obj)->string'''
        return f'Book with ID: {self.bookId}, Title: {self.title}, Author: {self.author}, Price: ${self.price},Rating: {self.rating}'

    def __eq__(self,other):
        ''' if ob1 == ob2: ...'''
        if not isinstance(other, Book):
            return NotImplemented
        return self.bookId == other.bookId

    def show(self):
        print(f'''
                Book with ID: {self.bookId}
                Title: {self.title}
                Author: {self.author}
                Price: ${self.price}
                Rating: {self.rating}
              ''')

   # ~~Не работи този метод~~ 
   # def getAllBooks(self, books):
   #     for book in books:
   #         print(f'''
   #             Book with ID: {book.bookId}
   #             Title: {book.title}
   #             Author: {book.author}
   #             Price: ${book.price}
   #             Rating: {book.rating}
   #           ''')

    def getBook(self):
        for book in self.books:
          if self.bookId == book.bookId:
              print(f'''
                  Book with ID: {self.bookId}
                  Title: {self.title}
                  Author: {self.author}
                  Price: ${self.price}
                  Rating: {self.rating}
                ''')
            

    def updateBook(self, book_id, book_title, book_author, book_price, book_rating):
        self.bookId = book_id
        self.title = book_title
        self.author = book_author
        self.price = book_price
        self.rating = book_rating
    
    #~~Не работи~~
    #def deleteBook(self):
    #    for book in self.books:
    #      self.books.pop(book)
        


if __name__ == '__main__':

    b1 = Book(1,"Harry Potter and the Order of the Phoenix", "J.K. Rowling", 12.66, 5)
    Book.books.append(b1)

    b2 = Book(2, "Carrie", "Stepen King", 16.99, 7)
    Book.books.append(b2)

    b3 = Book(3, "Every day", "David Levithan", 15.99, 10)
    Book.books.append(b3)

    b4 = Book(1,"Harry Potter and the Order of the Phoenix", "J.K. Rowling", 12.66, 5)
    Book.books.append(b4)

    Book.getBook(b1)

    #Book.getAllBooks(Book.books)

    b1.updateBook(1, "Harry Potter and the Deathly Hollows", "J.K. Rowling", 18.99, 5)

    b1.show()

    if b1 == b4:
        print("B1 and B2 are equal")

    print(str(b3))