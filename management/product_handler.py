
from menu import products


def get_product_by_id(product_id):
    for product in products:
        if product.get("_id") == product_id:
            return product
        return {}


def get_products_by_type(product_type):
    matched_products = []
    for product in products:
        if product.get("type") == product_type:
            matched_products.append(product)
    return matched_products
