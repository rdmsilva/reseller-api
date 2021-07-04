from marshmallow import Schema, fields


class PurchaseSchema(Schema):
    code = fields.String(required=True)
    value = fields.Float(required=True)
    date = fields.Date(required=True)
    cpf = fields.String(required=True)
    status = fields.String(required=False)
