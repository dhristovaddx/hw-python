from library.book import Book
from library.novel import Novel

class BookUtils:

    @staticmethod
    def calculateTotal(b1,b2):
        if not isinstance(b1,Book) or not isinstance(b2, Book):
            raise TypeError('params must be instances of Point')
        total = b1.price + b2.price
        return total
    
    @staticmethod
    def averageRating(*args):
        suma = 0
        for b in args:
            suma += int(b.rating) 
        
        avg = float(suma / len(args))
        return avg

if __name__ == '__main__':
    

    b1 = Book(1,"Harry Potter and the Order of the Phoenix", 12.66, 5)
    b2 = Book(2, "Carrie", 16.99, 7)
    b3 = Novel(3, "Every day", "YA", 15.99, 10)
    b4 = Novel(1,"Harry Potter and the Order of the Phoenix", "Fantasy", 12.66, 5 )
    b5 = Book.fromBook(b2)

    b5.show()

    #Въпрос: Защо като използвам show изписва Book1: None в output-a?
    print(f'''Order #1:
            Book 1: 
            {b1.show()}
            Book 2: 
            {b2.show()}
            Total Price: {BookUtils.calculateTotal(b1, b2)} ''')


    if b1 == b4:
        print("B1 and B4 are equal")

    #Demonstation of str
    print(str(b2))

    #Demonstration of averageRating
    print(f'Average rating of b1, b2, b3, b4 is: {BookUtils.averageRating(b1, b2, b3, b4)}')
    print(f'Average rating of b1, b2 is: {BookUtils.averageRating(b1, b2)}')

