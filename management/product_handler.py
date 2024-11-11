from menu import products


def get_product_by_id(product_id):
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product.get("_id") == product_id:
            return product
    return {}


def get_products_by_type(product_type):

    if not isinstance(product_type, str):
        raise TypeError("product type must be a str")

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


def menu_report():
    product_count = len(products)
    total_price = sum(product["price"] for product in products)
    average_price = total_price / product_count

    type_counts = {}

    for product in products:
        product_type = product["type"]
        if product_type in type_counts:
            type_counts[product_type] += 1
        else:
            type_counts[product_type] = 1

    most_common_type = max(type_counts, key=type_counts.get)

    report = (
        f"Products Count: {product_count} - "
        f"Average Price: ${average_price:.2f} -"
        f"Most Common Type: {most_common_type}"
    )

    return report
