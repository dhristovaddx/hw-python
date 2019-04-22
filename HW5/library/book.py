class Book:
    count = 0

    def __init__(self, bookId=0, title = '', price = 0, rating = 0):
      self.bookId = bookId
      self.title = title
      self.price = price
      self.rating = rating
  
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
        return f'Book with ID: {self.bookId}, Title: {self.title}, Price: ${self.price},Rating: {self.rating}'

    def __eq__(self,other):
        ''' if ob1 == ob2: ...'''
        if not isinstance(other, Book):
            return NotImplemented
        return self.bookId == other.bookId

    def show(self):
        print(f'''
                Book with ID: {self.bookId}
                Title: {self.title}
                Price: ${self.price}
                Rating: {self.rating}
              ''')

    def updateBook(self, book_id, book_title, book_price, book_rating):
        self.bookId = book_id
        self.title = book_title
        self.price = book_price
        self.rating = book_rating

    @classmethod
    def fromBook(cls,b):
        if not isinstance(b,cls):
            raise TypeError(f'param must be {cls}')
        return cls(b.bookId, b.title, b.price, b.rating)


