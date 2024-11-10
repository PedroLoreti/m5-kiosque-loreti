
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


def add_product(menu, **kwargs):
    existing_ids = []

    for product in menu:
        existing_ids.append(product["_id"])

    next_id = max(existing_ids, default=0) + 1

    new_product = {"_id": next_id, **kwargs}
    menu.append(new_product)

    return new_product
