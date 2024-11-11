
from management.product_handler import get_product_by_id


def calculate_tab(table_consumptions):
    subtotal = 0

    for consumption in table_consumptions:
        product_id = consumption["_id"]
        amount = consumption["amount"]

        product = get_product_by_id(product_id)

        product_price = product["price"]
        subtotal += product_price * amount

        subtotal = round(subtotal, 2)
    return {"subtotal": f"${subtotal}"}
