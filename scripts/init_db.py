import pandas as pd
from sqlalchemy import create_engine
from app.models.base import Base
from app.models.user import User
from app.models.product import Product
from app.models.event import Event

DATABASE_URL = "sqlite:///test.db"

def init_database():
    engine = create_engine(DATABASE_URL)

    # Create all tables
    Base.metadata.create_all(engine)

    try:
        users = pd.read_csv("data/users.csv")
        products = pd.read_csv("data/products.csv")
        events = pd.read_csv("data/events.csv")

        users.to_sql("users", engine, if_exists="append", index=False)
        products.to_sql("products", engine, if_exists="append", index=False)
        events.to_sql("events", engine, if_exists="append", index=False)

        print("Data loaded successfully")
    except FileNotFoundError:
        print("CSV files not found. Skipping data load.")

if __name__ == "__main__":
    init_database()