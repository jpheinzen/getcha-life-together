import datetime as dt
import typing   # can't seem to get this to work, but I want to try...?


class Account:
    """Base Account Class"""

    # List to keep track of transactions
    transactions = []

    # information about the account
    name: str       # The ':' seems to be a typing thing, but doesn't work to me right now... str doesn't even show up in a color.
    bank: str
    cDate: dt.time()
    eDate: None

    def __init__(self, name, bank, creationDate, endDate) -> None:
        self.name = name
        self.bank = bank
        self.cDate = creationDate
        self.eDate = endDate


class Savings(Account):
    """Savings Accounts"""
    # interest rate of savings account (in %) - eg. 0,1,etc
    intRate: float

    def __init__(self, name, bank, creationDate, endDate, interestRate) -> None:
        self.intRate = interestRate
        super().__init__(name, bank, creationDate, endDate)


class CreditCard(Account):
    """Account for a Credit Card"""

    # Date that the bill is DUE every month
    billDay: dt.time()

    def __init__(self, name, bank, creationDate, endDate, billDay) -> None:
        self.billDay = billDay
        super().__init__(name, bank, creationDate, endDate)
