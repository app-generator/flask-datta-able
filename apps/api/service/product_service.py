from flask_restx import Resource
from apps.models import Product
from marshmallow import fields, ValidationError
from apps.authentication.models import Users
from apps.helpers import validateCurrency
from apps.messages import Messages
from apps.config import Config

Currency = Config.CURRENCY
message = Messages.message


class ProductService(Resource):
    
    def create(self, user_id, request_data):
        name = request_data['name'] 
        information = request_data['information']
        description = request_data['description']
        price = request_data['price']

        # user not none
        if user_id is not None:
            # check user
            self.checkUser(user_id)
        
        new_product = Product(
        user_id = user_id,
        name = name,
        information = information,
        description = description,
        price = price
        )
        new_product.save()
        return new_product
    
    def update(self,user_id, id, request_data):
        currency = request_data['currency']

        # user not none
        if user_id is not None:
            # check user
            self.checkUser(user_id)
            
        # check currency
        validateCurrency(currency)
       
        product = Product.find_by_id(id)
        product.name  = request_data['name']
        product.information = request_data['information']
        product.description = request_data['description']
        product.price = request_data['price']
        product.currency  = currency

        product.save()
        return product
    
    def checkUser(self, user_id):
        """ check user """
        user = Users.find_by_id(user_id)
        # check user
        if not user:
            raise ValidationError(message['user_not_found'], 422)