import datetime as dt
import typing   # can't seem to get this to work, but I want to try...?
import pandas as pd


class Account:
    """Base Account Class"""

    # List to keep track of transactions
    transactions: pd.DataFrame()

    # information about the account
    name: str       # The ':' seems to be a typing thing, but doesn't work to me right now...
    bank: str
    cDate: dt.time()
    eDate: None

    def __init__(self, name, bank, creationDate, endDate) -> None:
        self.name = name
        self.bank = bank
        self.cDate = creationDate
        self.eDate = endDate

    def writeTransactions(self, transactions) -> bool:
        # Writes the transaction dataframe to a txt file of some sort, returning if success or fail
        return

    def readTransactions(self) -> bool:
        # read in transactions from file, setting transactions variable - try to do only once when you start program
        # self.transactions = ...
        return

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


class CCPoints(Account): # maybe we don't want this to inherit from account, but just hold a credit card..? maybe inherit from credit card...? not sure
    """Account to hold number of Credit Card Points"""
    
    cc: CreditCard
    points: float

    def __init__(self, creditCard, startPoints) -> None:
        self.cc = creditCard
        self.points = startPoints

        super().__init__(creditCard.name, creditCard.bank, creditCard.creationDate, creditCard.endDate)