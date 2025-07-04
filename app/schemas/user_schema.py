from app.extensions import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)
    is_admin = fields.Bool(dump_only=True)

user_schema = UserSchema()