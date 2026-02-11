# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math 

def is_valid_measurements_data(values) -> bool: 
    """Validates an iterable of measurement values. It ensures that the values input is a 
    non-empty and non-None iterable (list, tuple, set, range). If the input is valid, it returns 
    True; otherwise, it returns False.
    Args: 
      values: An iterable containing the measurement data to be validated.
    Returns: 
      True if the values parameter is a non-empty and non-None iterable of the correct type, 
      False otherwise.
    Example: 
      > is_valid_measurements_data([])
      False
      > is_valid_measurements_data([10, 99, 11.5, 21.5])
      True
      > is_valid_measurements_data("abc")
      False
      > is_valid_measurements_data([20, 30, None, 50])
      True"""
    # Validation: Check if input is empty, None, or not an allowed iterable type. Return False 
    # if the 'values' parameter is invalid, True otherwise.
    if not values or (not isinstance(values, (list, tuple, set, range))):
        return False 
    return True 
    
def is_valid_measurement(value) -> bool:
    """Validates a single measurement. If the measured value is valid, it returns 
    True; otherwise, it returns False. A valid measurement is a non-None value 
    that can be converted to a finite float (not Infinity (Inf) of Not-a-Number (NaN)) 
    and is not a boolean (since bools are subclasses of int in Python).
    Args: 
      value: The measurement value to be validated. 
    Returns: 
      True if the value is a valid measurement, False otherwise.
    Example: 
      > is_valid_measurement(11)
      True
      > is_valid_measurement(19.3)
      True
      > is_valid_measurement("22.5")
      True
      > is_valid_measurement("invalid")
      False
      > is_valid_measurement(None)
      False
      > is_valid_measurement(float('inf'))
      False
      > is_valid_measurement("")
      False"""
    # Type Validation: Ensure that the value is not None and is not a boolean (bools are subclasses of int).
    # Return False if the measurement is invalid, True otherwise. 
    if value is not None and (not (isinstance(value, bool))):
        try: 
            # Type Conversion: Attempt to cast the value to a float.
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