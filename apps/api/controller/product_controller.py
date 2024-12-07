from flask import  request
from flask_restx import Resource
from apps.api.exception import InvalidUsage
from apps.models import Product
from apps.api.schemas.product_schema import ProductSchema, ProductUpdateSchema
from apps.api.controller.base_contoller import BaseController
from apps.api.service.product_service import ProductService
from apps.helpers import token_required
from apps.messages import Messages
message = Messages.message

# base controller
BaseController = BaseController()
# schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
product_update_schema = ProductUpdateSchema()
# services
product_service = ProductService()


class ProductCreateList(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    @token_required
    def post(self):
        try:
            request_data = request.json
            # validate data
            product_schema.load(request_data)
            product = product_service.create(self.id, request_data)
            data = product_schema.dump(product)

            return BaseController.success(data,  message['record_created_successfully'])
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)
        
    @classmethod
    def get(self):
        try:
            products = Product.query.order_by(Product.id.desc()).all()
            response = products_schema.dump(products)
            
            return BaseController.send_response(response, 200)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)


   
class ProductList(Resource):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @classmethod
    def get(self, id):
        try:   
            result = Product.find_by_id(id)
            # check record exists or not
            if result is None:
                return BaseController.error(message['not_exists'], 422)
            
            response = product_schema.dump(result)

            return BaseController.send_response(response, 200)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)

    @classmethod
    @token_required
    def put(self, id):
        try:
            request_data = request.json
            product = Product.find_by_id(id)
            # check record exists or not
            if product is None:
                return BaseController.error(message['not_exists'], 422)
    
            # validate data
            product_update_schema.load(request_data)
            product = product_service.update(self.id, id, request_data)
            data = product_update_schema.dump(product)

            return BaseController.success(data, message['record_updated'], 200)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)
    
    @classmethod
    @token_required
    def delete(self, id):
        try:
            product = Product.find_by_id(id)
            # check record exists or not
            if product is None:
                return BaseController.error(message['not_exists'], 422)
            
            product.delete()

            return BaseController.simple_response(message['deleted_successfully'], 200)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)
