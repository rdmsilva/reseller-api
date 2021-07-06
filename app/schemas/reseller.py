from marshmallow import Schema, fields


class ResellerSchema(Schema):
    cpf = fields.Integer(required=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
