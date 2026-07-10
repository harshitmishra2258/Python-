class Products:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Products.count +=1

    @classmethod
    def get_count(cls):
        print (f"{cls.count}")
    
    def get_info(self):
        print(f"{self.name} is of Rs.{self.price}")

    @staticmethod
    def get_discount(price,discount):
        final_price = price - (price * discount / 100)
        print(f"{final_price}")

p1=Products("pen",10)
p2=Products("Laptop",50000)
p1.get_discount(10,1)

p1.get_info()

Products.get_count()

