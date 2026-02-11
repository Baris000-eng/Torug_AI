# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math 

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

    # Validation: Check if input is empty, None, or not an allowed iterable type.
    if not values or (not isinstance(values, (list, tuple, set, range))):
        return 0.0

    total = 0.0
    valid_count = 0

    # Iteration: Loop through each item in the iterable.
    for v in values:
        # Validation: Ensure value is not None and not a boolean (bools are subclasses of int).
        if v is not None and (not (isinstance(v, bool))):
            try:
                # Conversion: Attempt to cast the value to a float.
                num = float(v)
                
                # Safety Check on the Value: Ensure the number is finite (exclude NaN or Infinity).
                if math.isfinite(num):
                    total += num
                    valid_count += 1
                else:
                    continue
                    
            except:
                continue
        
    # ZeroDivisionError Prevention: Avoid divide-by-zero error if no valid measurements were found.
    if valid_count == 0:
        return 0.0

    # Calculation: Return the arithmetic mean of valid measurements. 
    return total / valid_count


# print(average_valid_measurements(range(1, 5)))