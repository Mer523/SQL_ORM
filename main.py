import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Stock, Shop, Sale

DSN = ""

engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

def get_shops(id_or_name):
    request = session.query(
        Book.title, Shop.name, Sale.price, Sale.date_sale,
        ).select_from(Shop). \
        join(Stock, Stock.shop_id == Shop.id). \
        join(Book, Book.id == Stock.book_id). \
        join(Publisher, Publisher.id == Book.publisher_id). \
        join(Sale, Sale.stock_id == Stock.id)

    print(f'{"Book": ^40} | {"Shop": ^10} | {"Price": ^8} | {"Date": ^10}')
    if id_or_name.isdigit():
        request = request.filter(Publisher.id == id_or_name).all()
        for book_title, shop_name, price, date_sale in request:
            print(f'{book_title: <40} | {shop_name: <10} | '
                  f'{price: < 8} | {date_sale.strftime("%d-%m-%Y")}')
    else:
        request = request.filter(Publisher.name == id_or_name).all()
        for book_title, shop_name, price, date_sale in request:
            print(f'{book_title: <40} | {shop_name: <10} | '
                  f'{price: < 8} | {date_sale.strftime("%d-%m-%Y")}')


if __name__ == '__main__':
    create_tables(engine)
id_or_name = input(
    "Введите id или название издательства: ")
print(get_shops(
    id_or_name))

session.close
