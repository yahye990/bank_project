from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ssn = Column(String, unique=True, nullable=False)

    accounts = relationship("Account", back_populates="customer")




class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(String, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    amount = Column(Numeric, nullable=False)
    currency = Column(String, nullable=False)
    sender_account = Column(String, nullable=False)
    receiver_account = Column(String, nullable=False)
    sender_country = Column(String, nullable=False)
    sender_municipality = Column(String, nullable=False)
    receiver_country = Column(String, nullable=False)
    receiver_municipality = Column(String, nullable=False)
    transaction_type = Column(String, nullable=False)
    notes = Column(String, nullable=False)

    def __init__(self,transaction,
                 timestamp,
                 amount,
                 currency,
                 sender_account,
                 receiver_account,
                 sender_country,
                 sender_municipality,
                 receiver_country,
                 receiver_municipality,
                 transaction_type,
                 notes):
        self.transaction_id = transaction
        self.timestamp = timestamp
        self.amount = amount
        self.currency = currency
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.sender_country = sender_country
        self.sender_municipality = sender_municipality
        self.receiver_country = receiver_country
        self.receiver_municipality = receiver_municipality
        self.transaction_type = transaction_type
        self.notes = notes


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True, nullable=False)
    balance = Column(Numeric, default=0)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", back_populates="accounts")