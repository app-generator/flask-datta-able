# Model Schemas
from ...models import Sale
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from apps import db


class SaleSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        fields = ("id", "product", "state", "value", "fee", "currency", "client", "payment_type", "purchase_date")
        model = Sale
        # strict = True
        sqla_session = db.session
    product         = fields.Integer(strict=True,  required=True)
    state           = fields.String(strict=True,  required=True)
    value           = fields.Integer(strict=True,  required=True)
    fee             = fields.Integer(strict=True,  required=False)
    payment_type    = fields.String(strict=True,   required=False)
    client          = fields.String(strict=True,   required=False)
    purchase_date   = fields.String(strict=True,   required=False)
    # user_id         = fields.Integer(required=False)
 

class SaleUpdateSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        fields = ("id", "product", "state", "value", "fee", "currency", "client", "payment_type", "purchase_date")
        model = Sale
        # strict = True
        sqla_session = db.session
    product         = fields.Integer(strict = True, required=True)
    state           = fields.String(strict = True,  required=True)
    value           = fields.Integer(strict = True, required=True)
    fee             = fields.Integer(strict = True, required=True)
    currency        = fields.String(strict = True,  required=True)
    client          = fields.String(strict = True,  required=True)
    payment_type    = fields.String(strict = True,  required=True)
    # purchase_date   = fields.String(strict = True,  required=True)
    # user_id         = fields.Integer(required=False)
