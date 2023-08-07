from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float

from db.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    fullname = Column(String)
    username = Column(String)
    balance = Column(Float)
    is_active = Column(Boolean, default=True)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    limit = Column(Integer, index=True)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = ForeignKey("Category")
    amount = Column(Integer, index=True)


class TakenBook(Base):
    __tablename__ = "takenbooks"
    id = Column(Integer, primary_key=True, index=True)
    book = ForeignKey("Book")
    user = ForeignKey("User")
    taken_date = Column(String, index=True)
    returning_date = Column(String, index=True)
    bill = Column(Float, index=True)
