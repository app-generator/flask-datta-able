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
from apps.config import Config

Currency = Config.CURRENCY
PAYMENT_TYPE = Config.PAYMENT_TYPE


class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    user_id       = db.Column(db.Integer,      default=1)
    name          = db.Column(db.String(128),  nullable=False)
    information   = db.Column(db.String(128),  nullable=False)
    description   = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.String(10),   default=Currency['usd'], nullable=False)
    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

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
    state         = db.Column(db.Integer,     nullable=False)
    value         = db.Column(db.Integer,     nullable=False)
    fee           = db.Column(db.Integer,     default=0)
    currency      = db.Column(db.String(10),  default=Currency['usd'], nullable=False)
    client        = db.Column(db.String(128), nullable=True)
    payment_type  = db.Column(db.Integer(),   default=PAYMENT_TYPE['cc'], nullable=False)
    purchase_date = db.Column(db.DateTime,    default=dt.datetime.utcnow())
    creation_date = db.Column(db.DateTime,    default=dt.datetime.utcnow())
    update_date   = db.Column(db.DateTime,    default=db.func.current_timestamp(),
                                              onupdate=db.func.current_timestamp())

    @classmethod
    def find_by_id(cls, _id: int) -> "Sale":
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
