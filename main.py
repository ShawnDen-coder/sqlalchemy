from sqlalchemy import *
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from datetime import datetime

Base = declarative_base()

url = 'postgresql+psycopg2://root:denghui123@47.101.155.174:5432/pytest'
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


class Cookie(Base):
    __tablename__ = "cookies"
    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(10, 2))


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    create_on = Column(DateTime(), default=datetime.now)
    update_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    user = relationship("User", backref('orders', order_by=order_id))


class LineItems(Base):
    __tablename__ = 'line_items'
    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey("orders.order_id"))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(10, 2))
    order = relationship("Order", backref=backref("line_items", order_by=line_item_id))
    cookie = relationship("Cookie", uselist=False, order_by=id)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

