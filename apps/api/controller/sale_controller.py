from flask_restx import Resource
from flask import request
from apps.api.exception import InvalidUsage
from apps.models import Sale
from apps.api.schemas.sale_schema import SaleSchema, SaleUpdateSchema
from apps.api.controller.base_contoller import BaseController
from apps.api.service.sale_service import SaleService
from apps.helpers import token_required
from apps.messages import Messages
message = Messages.message

# base controller
BaseController = BaseController()
# schemas
sale_schema = SaleSchema()
sales_schema = SaleSchema(many=True)
sale_update_schema = SaleUpdateSchema()
# services
sale_service = SaleService()


class SaleCreateList(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    @token_required
    def post(self):
        try:
            request_data = request.json
            # validate data
            sale_schema.load(request_data)
            sale = sale_service.create(self.id, request_data)
            data = sale_schema.dump(sale)

            return BaseController.success(data, message['record_created_successfully'], 201)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)
        
    @classmethod
    def get(self):
        try:
            sales = Sale.query.order_by(Sale.id.desc()).all()
            response = sales_schema.dump(sales)
            
            return BaseController.send_response(response, 200)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)


   
class SaleList(Resource):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @classmethod 
    def get(self, id):
        try:
            result = Sale.find_by_id(id)
            # check record exists or not
            if result is None:
                return BaseController.error(message['not_exists'], 422)
            
            response = sale_schema.dump(result)

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
            sale = Sale.find_by_id(id)
            # check record exists or not
            if sale is None:
                return BaseController.error(message['not_exists'], 422)

            # validate data
            sale_update_schema.load(request_data)
            sale = sale_service.update(id, request_data)
            data = sale_update_schema.dump(sale)

            return BaseController.success(data, message['record_updated'], 200)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)
    
    @classmethod
    @token_required
    def delete(self, id):
        try:
            sale = Sale.find_by_id(id)
            # check record exists or not
            if sale is None:
                return BaseController.error(message['not_exists'], 422)
            
            sale.delete()

            return BaseController.send_response(message['deleted_successfully'], 200)
        except InvalidUsage as e:
            return BaseController.error(e, 422)
        except BaseException as e:
            return BaseController.errorGeneral(e)
