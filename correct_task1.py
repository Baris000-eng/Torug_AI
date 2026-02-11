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
    # Validation: Check if orders is empty, None, or not an allowed iterable type.
    if not orders or (not isinstance(orders, (list, tuple, set))):
        return 0.0

    total = 0.0
    valid_count = 0

    for order in orders:
        # Type Checking: Attempt to convert order to a dictionary (e.g., if it's a tuple of tuples).
        try:
            order = dict(order)
        except:
            continue # Skip if the item cannot be converted to a dictionary.

        # Structure Checking: Ensure required keys 'status' and 'amount' exist.
        if "status" in order and "amount" in order:
            
            # Data Cleaning: Normalize status to lowercase to handle 'Cancelled', 'CANCELLED', etc.
            try:
                order_status = str(order["status"]).lower()
            except:
                continue # Skip if status cannot be converted to a string.
            
            # Filtering: Skip orders that were cancelled or canceled (US/UK spelling).
            if order_status not in ["cancelled", "canceled"]:
                
                # Type Conversion & Validation: Attempt to convert amount to float.
                try:
                    amount = float(order["amount"])
                    
                    # Safety Check: Ensure the number is finite (exclude NaN or Infinity).
                    if math.isfinite(amount):
                        total += amount
                        valid_count += 1
                except:
                    continue # Skip if amount cannot be converted to a float.
        
    # Error Prevention: Avoid division-by-zero if no valid orders were found.
    if valid_count == 0: 
        return 0.0 

    # Calculation: Compute and return the arithmetic mean.
    return total / valid_count