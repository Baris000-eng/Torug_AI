# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math 

def average_valid_measurements(values):

    if not values or (not isinstance(values, (list, tuple, set))):
        return 0.0

    total = 0.0
    valid_count = 0

    for v in values:
        if v is not None:
            try:
                num = float(v)
                
                if math.isfinite(num):
                    total += num
                    valid_count += 1
                else:
                    continue
                    
            except:
                continue
        
    # To avoid division by zero, return 0.0 if there are no valid measurements.
    if valid_count == 0:
        return 0.0

    return total / valid_count