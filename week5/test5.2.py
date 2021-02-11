import os
product = []
price = []
class Shop :
    def menu(self) :
        global choose
        print('*'*10+'Coconut Shop')

    def __str__(self) :
        print("{0: <20}{1: <15}{2: <10}".format(self.product, self.price, self.amount))




while True :
    