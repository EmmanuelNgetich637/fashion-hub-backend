from app.extensions import ma
from app.models.product import Product

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

        id = ma.auto_field()
        name = ma.auto_field()
        price = ma.auto_field()
        description = ma.auto_field()
        stock = ma.auto_field()

        load_instance = True

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
        