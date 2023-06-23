import sqlalchemy as sqa
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sqa.Column(sqa.Integer, primary_key=True)
    name = sqa.Column(sqa.String(length=40), nullable=False, unique=True)

    def __str__(self):
        return f"Издатель {self.id}: {self.name}"


class Book(Base):
    __tablename__ = "book"

    id = sqa.Column(sqa.Integer, primary_key=True)
    title = sqa.Column(sqa.String(length=40), nullable=False)
    id_publisher = sqa.Column(sqa.Integer, sqa.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")


class Shop(Base):
    __tablename__ = "shop"

    id = sqa.Column(sqa.Integer, primary_key=True)
    name = sqa.Column(sqa.String(length=40), nullable=False, unique=True)

    def __str__(self):
        return f"Магазин {self.id}: {self.name}"


class Stock(Base):
    __tablename__ = "stock"

    id = sqa.Column(sqa.Integer, primary_key=True)
    id_book = sqa.Column(sqa.Integer, sqa.ForeignKey("book.id"), nullable=False)
    id_shop = sqa.Column(sqa.Integer, sqa.ForeignKey("shop.id"), nullable=False)
    count = sqa.Column(sqa.Integer, nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")


class Sale(Base):
    __tablename__ = "sale"

    id = sqa.Column(sqa.Integer, primary_key=True)
    price = sqa.Column(sqa.Integer, nullable=False)
    date_sale = sqa.Column(sqa.Date, nullable=False)
    id_stock = sqa.Column(sqa.Integer, sqa.ForeignKey("stock.id"), nullable=False)
    count = sqa.Column(sqa.Integer, nullable=False)

    stock = relationship(Stock, backref="sale")


def create_tables(engine):
    Base.metadata.create_all(engine)