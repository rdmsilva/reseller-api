from marshmallow import Schema, fields


class PurchaseSchema(Schema):

    id = fields.Integer(required=False)
    code = fields.String(required=True)
    value = fields.Float(required=True)
    date = fields.Date(required=True)
    cpf = fields.Integer(required=True)
    status = fields.String(required=False)
    percent = fields.Float(required=False, dump_only=True)
    cashback = fields.Float(required=False, dump_only=True)
