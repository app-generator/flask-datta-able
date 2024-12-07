from flask_restx import Resource
from apps.models import Product, Sale
from marshmallow import ValidationError
from apps.authentication.models import Users
from apps.helpers import validateCurrency, validatePaymentMethod, validateState
from apps.messages import Messages

message = Messages.message


class SaleService(Resource):
    
    def create(self, user_id, request_data):
        product = request_data.get('product')
        value = request_data.get('value')
        currency = request_data.get('currency')
        fee = request_data.get('fee') 
        client = request_data.get('client')

        # user not none
        if user_id is not None:
            # check user
            self.checkUser(user_id)
        else:
            raise ValidationError("user id required", 422)
    
        # check state
        state = validateState(request_data.get('state'))
        # check payment method
        payment_type = validatePaymentMethod(request_data.get('payment_type'))
        # check currency
        validateCurrency(currency) 

        result = Product.find_by_id(product)
        # check record exists or not
        if result is None:
            raise ValidationError(message['product_not_exists'], 422)
        
        new_sale = Sale(
            product = product,
            state = state,
            value = value,
            fee = fee,
            currency = currency,
            client = client,
            payment_type = payment_type,
            )

        new_sale.save()
        return new_sale
    
    def update(self, id, request_data):
        product = request_data.get('product') 
        value = request_data.get('value')
        currency = request_data.get('currency')
        fee = request_data.get('fee') 
        client = request_data.get('client')
        
        user_id = request_data.get('user_id')
        # user not none
        if user_id is not None:
            # check user
            self.checkUser(user_id)

        # check state
        state = validateState(request_data.get('state'))
        # check payment method
        payment_type = validatePaymentMethod(request_data.get('payment_type'))
        # check currency
        validateCurrency(currency) 
    
        result = Product.find_by_id(product)
        # check record exists or not
        if result is None:
            raise ValidationError(message['product_not_exists'], 422)
        
        sale = Sale.find_by_id(id)
        sale.product  = product
        sale.state = state
        sale.value = value
        sale.fee = fee
        sale.currency = currency
        sale.client = client
        sale.payment_type = payment_type

        sale.save()
        return sale
    
    def checkUser(self, user_id):
        """ check user """
        user = Users.find_by_id(user_id)
        # check user
        if not user:
            raise ValidationError(message['user_not_found'], 422)