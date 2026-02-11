# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

import math

def is_valid_orders_data(orders): 
    """It validates a collection of orders. It ensures that the orders input is a non-empty and non-None iterable (list, tuple, set).
    Args: 
        orders: An iterable containing order data.
    Returns: 
        True if the orders parameter is a non-empty and non-None iterable of the correct type, False otherwise."""
    # Validation: Check if input is empty, None, or not an allowed iterable type.
    # Return False if the parameter is invalid, True otherwise.
    if not orders or (not isinstance(orders, (list, tuple, set))):
        return False 
    return True 

def is_valid_order(order) -> bool:
    """Checks if an order has the required structure and is not cancelled.
    An order is considered valid if: 
    - It can be cast to a dictionary.
    - It contains the keys 'status' and 'amount'.
    - The order status is not 'cancelled' in a case-insensitive manner (e.g., 'CANCELLED', 'cANcELLeD', 'Cancelled', etc.).
    Args: 
        order: The order to be validated, which has ideally a dictionary-like structure.
    Returns:
        True if the order is valid, False otherwise."""
    # Type Checking: Attempt to convert order to a dictionary structure.
    try:
        order = dict(order)
    except:
        # Skip if the item cannot be converted to a dictionary.
        return False 

    # Structure Checking: Ensure required keys 'status' and 'amount' exist.
    if "status" in order and "amount" in order:
            
        # Data Cleaning: Normalize status to lowercase to handle 'Cancelled', 'CANCELLED', etc.
        try:
            order_status = str(order["status"]).lower()
        except:
            # Skip if status cannot be converted to a string.
            return False 
            
        # Filtering: Skip orders that were cancelled or canceled (UK/US spelling).
        return order_status not in ["cancelled", "canceled"]
    
    # If the order does not have the required keys, it is considered invalid.
    return False 

def is_valid_order_amount(amount) -> bool: 
    """Checks if the order amount is a valid, finite number."""
    # Type Conversion & Validation: Attempt to convert amount to float.
    try: 
        num = float(amount)
        # Safety Check: Ensure the number is finite (exclude NaN (Not-a-Number) or Infinity). 
        return math.isfinite(num) 
    except: 
        # Return False if the amount cannot be converted to a float. 
        return False 

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
    if is_valid_orders_data(orders) == False: 
        return 0.0

    valid_total = 0.0
    valid_count = 0

    for order in orders:
        if is_valid_order(order): 
                amount = order["amount"]
                if is_valid_order_amount(amount):
                    valid_total += float(amount)
                    valid_count += 1
                else:
                    # Amount is invalid, so skip this order. 
                    continue 
        
        else:
            # Skip invalid orders
            continue
        
    # Error Prevention: Avoid division-by-zero if no valid orders were found.
    if valid_count == 0: 
        return 0.0 

    # Calculation: Compute and return the arithmetic mean.
    return valid_total / valid_count