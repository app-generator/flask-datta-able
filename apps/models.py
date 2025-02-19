# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class PAYMENT_TYPE(Enum):
    cc = 'cc'
    paypal = 'paypal'
    wire = 'wire'

class REFUNDED_TYPE(Enum):
    yes = 'yes'
    no = 'no'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    #currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


class Sale(db.Model):
    
    __tablename__ = 'sales'

    id            = db.Column(db.Integer,     primary_key=True)
    product       = db.Column(db.Integer,     db.ForeignKey("products.id", ondelete="cascade"), nullable=False)
    product_id    = relationship(Product,     uselist=False, backref="sales")
 
    buyerEmail    = db.Column(db.String(128), nullable=False)
    purchase_date = db.Column(db.DateTime,    default=db.func.current_timestamp())
    #payment_type  = db.Column(db.Enum(PAYMENT_TYPE), default=PAYMENT_TYPE.cc, nullable=False)
    country       = db.Column(db.String(128), default='USA')
    #refunded      = db.Column(db.Enum(REFUNDED_TYPE), default=REFUNDED_TYPE.no, nullable=False)
    quantity      = db.Column(db.Integer,     default=1)

    creation_date = db.Column(db.DateTime,    default=db.func.current_timestamp())
    update_date   = db.Column(db.DateTime,    default=db.func.current_timestamp(),
                                              onupdate=db.func.current_timestamp())

    @classmethod
    def find_by_id(cls, _id: int) -> "Sale":
        return cls.query.filter_by(id=_id).first() 

    def __repr__(self):
        return f"{self.product}"

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return
