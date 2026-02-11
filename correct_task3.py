# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math 

def is_valid_measurements_data(values): 
    """It validates an iterable of measurement values. It ensures that the values input is a 
    non-empty and non-None iterable (list, tuple, set, range). If the input is valid, it returns 
    True; otherwise, it returns False."""
    # Validation: Check if input is empty, None, or not an allowed iterable type. Return False if invalid,  True if valid.
    if not values or (not isinstance(values, (list, tuple, set, range))):
        return False 
    return True 
    
def is_valid_measurement(value):
    """It validates a single measurement. If the measured value is valid, it returns 
    True; otherwise, it returns False. A valid measurement is a non-None value 
    that can be converted to a finite float (not Infinity (Inf) of Not-a-Number (NaN)) 
    and is not a boolean (since bools are subclasses of int in Python)."""
    # Validation: Ensure value is not None and not a boolean (bools are subclasses of int).
    if value is not None and (not (isinstance(value, bool))):
        try: 
            # Conversion: Attempt to cast the value to a float.
            num = float(value)

            # Safety Check on the Value: Ensure the number is finite (exclude NaN (Not-a-Number) or infinity).
            if math.isfinite(num): 
                return True
        except: 
            return False 
    
    return False 

def average_valid_measurements(values):
    """
    Calculates the arithmetic mean of valid, finite numerical measurements.

    This function iterates through an iterable of potential measurements,
    filters out `None` values, attempts to convert remaining values to floats,
    and ensures they are finite numbers (not NaN or Infinity).

    It robustly handles:
    - Different iterable types (`list`, `tuple`, `set`, `range`).
    - Values that can be cast to float (e.g., strings containing numbers).
    - Non-finite numbers (`inf`, `-inf`, `nan`).
    - Invalid data types that cause `ValueError` during casting.

    Args:
        values: An iterable containing numerical data, strings representing
            numbers, or `None`.

    Returns:
        float: The average of the valid measurements. Returns **0.0** if
        the input is empty, invalid, or contains no valid numerical data.

    Example:
        > data = [5, "15", None, 40.5, float('nan'), float('inf')]
        > average_valid_measurements(data)
        20.166666666666668
    """

    if is_valid_measurements_data(values) == False:
         return 0.0

    valid_total = 0.0
    valid_count = 0

    # Iteration: Loop through each item in the iterable.
    for value in values:
        if is_valid_measurement(value):
            valid_total += float(value)
            valid_count += 1
        else:
             # Skip invalid measurement values.
             continue 
                    
    # ZeroDivisionError Prevention: Avoid divide-by-zero error if no valid measurements were found.
    if valid_count == 0:
        return 0.0

    # Calculation: Return the arithmetic mean of valid measurements. 
    return valid_total / valid_count


# print(average_valid_measurements(["10", "10.5", "20.5"]))