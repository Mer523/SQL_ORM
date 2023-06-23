import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale, create_tables


DSN = ""
engine = sqlalchemy.create_engine(DSN)

if __name__ == "__main__":
    create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


pub1 = Publisher(name="Буквоед")
pub2 = Publisher(name="Лабиринт")
pub3 = Publisher(name="Книжный дом")
session.add_all([pub1, pub2, pub3])
session.commit()

book1 = Book(title="Капитанская дочка", publisher=pub1)
book2 = Book(title="Руслан и Людмила", publisher=pub1)
book3 = Book(title="Капитанская дочка", publisher=pub2)
book4 = Book(title="Евгений Онегин", publisher=pub3)
session.add_all([book1, book2, book3, book4])
session.commit()

shop1 = Shop(name="Читай город")
shop2 = Shop(name="Дом Книги")
shop3 = Shop(name="Лабиринт")
session.add_all([shop1, shop2, shop3])
session.commit()

stock1 = Stock(book=book1, shop=shop1, count=600)
stock2 = Stock(book=book2, shop=shop1, count=500)
stock3 = Stock(book=book3, shop=shop3, count=580)
stock4 = Stock(book=book4, shop=shop2, count=490)
session.add_all([stock1, stock2, stock3, stock4])
session.commit()

sale1 = Sale(price=1200, date_sale='09-11-2022', stock=stock1, count=100)
sale2 = Sale(price=1300, date_sale='08-11-2022', stock=stock2, count=20)
sale3 = Sale(price=900, date_sale='05-11-2022', stock=stock3, count=85)
sale4 = Sale(price=1000, date_sale='2022-09-22', stock=stock4, count=200)
session.add([sale1, sale2, sale3, sale4])
session.commit()


pub_name = input('Название издательства: ')
pub_id = input('Идентификатор издательства: ')



def get_shop_by_publisher(publisher_name=None, publisher_id=None):
    if publisher_id is not None and publisher_name is None:
        for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).join(Book.publisher)\
                .filter(Publisher.id == int(publisher_id)):
            print(c)
    elif publisher_name is not None and publisher_id is None:
        for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).join(Book.publisher)\
                .filter(Publisher.name == publisher_name):
            print(c)
    elif publisher_name is not None and publisher_id is not None:
        for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).join(Book.publisher)\
                .filter(Publisher.name == publisher_name, Publisher.id == int(publisher_id)):
            print(c)

if __name__ == "__main__":
    get_shop_by_publisher(publisher_id=pub_id)

session.close()