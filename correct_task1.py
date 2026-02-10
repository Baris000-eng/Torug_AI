# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

import math

def calculate_average_order_value(orders):
    """
    Calculates the average monetary value of valid, non-cancelled orders.

    This function iterates through a collection of orders, validates that each
    order is a dictionary (or can be cast to one) containing 'status' and
    'amount' keys, filters out cancelled orders, ensures the amount is a
    finite number, and computes the arithmetic mean of the remaining amounts. 
    Moreover, it handles various edge cases seamlessly, such as empty/None
    inputs, non-iterable inputs, and orders with missing, malformed, and/or 
    incompatible data. 

    Args:
        orders: An iterable containing order data. Each order should ideally
            be a dictionary-like structure containing at least:
            - 'status' (str): The current status of the order (e.g., 'shipped', 
              'cancelled').
            - 'amount' (float/int/str): The monetary value of the order.

    Returns:
        float: The average order value. Returns **0.0** if the input is
        empty, invalid, or contains no valid, non-cancelled orders.

    Example:
        > orders = [
            > {'status': 'delivered', 'amount': 100.0},
            > {'status': 'shipped', 'amount': 50.0},
            > {'status': 'cancelled', 'amount': 200.0},
            > {'status': 'delivered', 'amount': '75.0'}
        > ]
        > calculate_average_order_value(orders)
        75.0
    """
    if not orders or (not isinstance(orders, (list, tuple, set))):
        return 0.0

    total = 0.0
    valid_count = 0

    for order in orders:
        try:
            order = dict(order)
        except:
            continue

        if "status" in order and "amount" in order:
            try:
                order_status = str(order["status"]).lower()
            except:
                continue
            if order_status not in ["cancelled", "canceled"]:
                try:
                    amount = float(order["amount"])
                    
                    if math.isfinite(amount):
                        total += amount
                        valid_count += 1
                except:
                    continue

    # To avoid division by zero, return 0.0 if there are no valid orders.
    if valid_count == 0: 
        return 0.0 

    return total / valid_count