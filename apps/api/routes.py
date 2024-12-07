# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps.api import blueprint
from apps.api.controller.product_controller import ProductCreateList, ProductList
from apps.api.controller.sale_controller import SaleCreateList, SaleList
from flask_restx import Api

# from flask_restx import Api
api = Api(blueprint, title="API", description="API")

# Product api's end points.
api.add_resource(ProductCreateList, '/products/')
api.add_resource(ProductList, '/products/<int:id>')

# Sale api's end points.
api.add_resource(SaleCreateList, '/sales/')
api.add_resource(SaleList, '/sales/<int:id>')