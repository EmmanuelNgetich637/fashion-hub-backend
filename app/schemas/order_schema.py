from app.extensions import ma
from app.models.order import Order

class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order

    id = ma.auto_field()
    user_id = ma.auto_field()
    product_id = ma.auto_field()
    quantity = ma.auto_field()
    total_price = ma.auto_field()

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
