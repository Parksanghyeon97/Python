class Book:

    bookstore = {}
    def __init__(self):
        print('책 객체를 새로 만들었어요')
    def setData(self, title, price, author):
        self.bookstore[title] = [price, author]
    def printData(self, title):
        if title in self.bookstore:
            print(self.bookstore[title])
        else:
            print('none')

        '''
        print('제목 : ', self.title)
        print('가격 : ', self.price)
        print('저자 : ', self.author)
        '''
