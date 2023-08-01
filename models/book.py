import datetime

from models.user import UserOut


class Category:
    name: str
    limit: int


class Book:
    category: Category
    amount: int
    name: str


class TakenBook:
    book: Book
    user: UserOut
    taken_date: datetime.datetime
    returning_date: datetime.datetime
    bill: float = 0.0
