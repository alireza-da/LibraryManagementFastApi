import datetime

from models.user import User


class Category:
    name: str
    limit: int


class Book:
    category: Category
    amount: int
    name: str


class TakenBook:
    book: Book
    user: User
    taken_date: datetime.datetime
    returning_date: datetime.datetime
    bill: float = 0.0
