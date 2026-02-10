# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

import math

def calculate_average_order_value(orders):

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