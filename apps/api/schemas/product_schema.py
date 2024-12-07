# Model Schemas
from ...models import Product
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from apps import db


class ProductSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        fields = ("id", "name", "information", "description", "price", "currency")
        model = Product
        sqla_session = db.session
    name        = fields.String(strict=True,   required=True)
    information = fields.String(strict=True,   required=True)
    price       = fields.Integer(strict=True,  required=True)


class ProductUpdateSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        fields = ("id", "name", "information", "description", "price", "currency")
        model = Product
        # strict = True
        sqla_session = db.session
    name        = fields.String(strict = True, required=True)
    information = fields.String(strict = True, required=True)
    price       = fields.Integer(strict=True,  required=True)
    currency    = fields.String(strict = True, required=True)
