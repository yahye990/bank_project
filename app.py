import pandas as pd
from db import init_db, SessionLocal
from models import Transaction
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import Column, Integer

id = Column(Integer, primary_key=True, autoincrement=True)

from decimal import Decimal
from datetime import datetime
import csv

def main():
    init_db()
    db = SessionLocal()
    print("start")

    try:
        #with db.begin():  # automatiskt commit om inget går fel
            with open('new_transactions_data.csv') as csvfile:
                reader = csv.DictReader(csvfile)
                for index, row in enumerate(reader):
                    try:
                        transaction = Transaction(
                            transaction=row["transaction_id"],
                            timestamp=row["timestamp"],
                            amount=row["amount"],
                            currency=row["currency"],
                            sender_account=row["sender_account"],
                            receiver_account=row["receiver_account"],
                            sender_country=row["sender_country"],
                            sender_municipality=row["sender_municipality"],
                            receiver_country=row["receiver_country"],
                            receiver_municipality=row["receiver_municipality"],
                            transaction_type=row["transaction_type"],
                            notes=row["notes"]
                        )
                        db.add(transaction)

                    except (ValueError, KeyError) as e:
                        print(f"Rad {index} hoppar över p.g.a. fel: {e}")
    except SQLAlchemyError as db_error:
        print(f"Databasfel: {db_error}")
    finally:
        db.close()
        print("klart")



    db.commit()

    #
    #except SQLAlchemyError as e:
       # db.rollback()
       # print("[ERROR] Något gick fel:", e)

    #try:
        #with db.begin():
           #customer = Customer(name="Benjamin", ssn="7001092456", email="benjamin@example.com")
            #db.add(customer)

            #account = Account(number="8064047892", balance=200, customer_id=customer.id)
            #db.add(account)

    #except SQLAlchemyError as e:
        #db.rollback()
        #print("[ERROR] Något gick fel:", e)

    #print(f"{customer.name} ({customer.email}) har saldo {account.balance}")

    db.close()

if __name__ == "__main__":
    main()