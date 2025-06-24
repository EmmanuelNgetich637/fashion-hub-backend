from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.schemas.product_schema import product_schema, products_schema
from app.extensions import db
from flask_jwt_extended import jwt_required

product_bp = Blueprint('products', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@product_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    errors = product_schema.validates(data)
    if errors:
        return jsonify(errors), 400
    
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product), 202

@product_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()

    for key, value in data.items():
        setattr(product, key, value)

    db.session.commit()
    return product_schema.jsonify(product)

@product_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})
