# AI Code Review Assignment (Python)

## Candidate
- Name: Barış Kaplan 
- Approximate time spent: 100 minutes (1 hour 40 minutes)

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The given code assumes that the "status" and "amount" keys are already existing in the dictionary named 'order'. However; if one of these keys is missing in the dictionary 'order', the function will raise a KeyError, regarding the missing key. 

- Irrespective of how many orders are cancelled, we are currently dividing the total order amount by the length (len(orders)) of the orders data structure (e.g. a list). This means that the count of the cancelled orders are still included in the divisor, even though they are excluded from the total order value. So, this will skew and give the wrong average order value at the end. 

- No type validation is performed on the orders, each order in the orders, and the values existing in each order. order["status"] might not be of type string (such as int, float, or None), which will cause error while comparing it with "cancelled". Moreover, order["amount"] can be a None, string, or a non-numeric value. This would cause a ValueError or TypeError. 

- Each order in orders data structure can be a data type other than a dictionary. We need to ensure that each order in orders to be a dictionary. 


### Edge cases & risks
- Orders data structure can be empty or None, or it can be a data type other than the list, tuple, or set. These cases are not handled in the current version of the code. 

- Order amounts with infinite values are included in the current version, which will skew the average order value calculation. 

- Order status check is done in a case-sensitive manner. One can type the order status value as "CANcelled". It will also mean that the order is cancelled and we need to do this check in a case-insensitive manner. If not, then we will skip such values of the order statuses, which will lead to a wrong average order value.

- For the empty input parameter of orders (such as list(), [], and tuple()), the count will be zero. Therefore, the current version of the code will throw divide-by-zero (ZeroDivision) error. We need to handle this in the code. 


- Order amounts can be accidentally given as NaN (Not-a-Number) values, which will directly make the average order value NaN. We should also avoid this scenario. 

- Free purchases (order["amount"] = 0), or completed but returned orders after completion (order["amount"] < 0) are included in the non-cancelled orders. Depending on the business requirements, we may prefer seperating these scenarios with different keys (such "free" and "returned"), or specify it in the docstring that the non-cancelled orders include/exclude the free purchases and/or the returned orders after completion. 



### Code quality / design issues
- Currently, the count and the total sum values are inconsistent with each other. The current version counts the invalid orders in the denominator, even though they are excluded from the total order value in the numerator. This will pull the average order value downwards. 

- There is no try-except block to catch the ZeroDivisionError that might happen while calculating the average value. Moreover, there is no if statement that checks whether 
the count is equal to 0 and then if so, proceed accordingly (e.g. return 0.0). We should add one of them to the code so that the divide-by-zero error (ZeroDivisionError) is avoided. 

- Irrespective of how many orders are cancelled, we are currently dividing the total order amount by the length (len(orders)) of the orders data structure (e.g. a list). This means that the count of the cancelled orders are still included in the divisor, even though they are excluded from the total order value. So, this will skew and give the wrong average order value at the end. In order to handle this problem, before the iteration over the orders starts (before the for loop), we should initialize the count with zero. Then, if the order status is not cancelled, we need to increment the count by one. At the end, we have found the number of non-cancelled orders. 

- In the current version, there is no docstring which gives a hint about the type of the orders parameter, and what type of values it includes. This will make the function harder to understand and/or maintain within a team. 

- There is no validation applied on the 'orders' data which is given as the parameter. This parameter should be a list/tuple/set of dictionaries. 

- There are no try-except blocks or type checks that are used to validate the types of order["status"] and order["amount"]. 

- There is no finiteness check on the status["amount"], we should check it so that we avoid infinite amounts or NaN (Not-a-Number) amounts given in the status dictionary. 


## 2) Proposed Fixes / Improvements
### Summary of changes
- Division-by-zero bug is fixed: 'count = len(orders)' is replaced with 'valid_count', and 
the valid_count is incremented only if the order is non-cancelled. An if statement checking whether the valid_count is 0 is added after the for loop. If so, we return 0.0 as the average. Through this if check, we can handle empty order parameter input (e.g. [] or list()) without any errors. 

- Input parameter validation is added: It checks if order is not a list/tuple/set, or is empty, and return 0.0 as the average order value if so. 

- Case insensitive order status comparison: Conversion of order["status"] to lowercase, before comparing it with the "cancelled", is added. This string value could be given as "cancelled" or "canceled". The "canceled" is preferred in the American English, and the "cancelled" is preferred in the British English. So, both of these versions are correct. 

- Safer key access is added: Verification of the existence of both the "status" and "amount" keys is added before using them. 

- Amount validation is improved: The amount (status["amount"]) is converted to float using the 
float() function within a try-except block. This will ensure that the amount is either a float or an integer. This conversion in the try-except block ensures that any amount values of incompatible types are safely ignored. Moreover, math.isfinite(amount) is used to ignore infinite or NaN values of the amount. 

- More robust order data handling is added: Each order in orders is safely typecasted/converted into a dictionary (dict()) within a try-except block. Each order that is not a dictionary type  (e.g. an integer) is handled and skipped. 

- Error tolerance is added: Risky operations such as typecasting (e.g. float() and dict()) are wrapped with try-except blocks so that the bad data does not crash the function. 


### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

1. Empty or invalid input parameters : Because, the function explicitly checks for non-iterable or empty inputs. 

2. Division by zero error protection is added: If all orders are cancelled (there are no valid orders), then the function returns 0.0.

3. Cancelled orders: The orders with status "cancelled" or "canceled", in a case-insensitive manner, should be skipped. 

4. Non-numeric or invalid amount (status["amount"]) values: The function tries to convert the amount fo float, using float() function, and ignores invalid types of the amount data. 

5. Mixed data types in orders: The function tries to convert each order to a dictionary, using dict() function. So, we should test for different types of data for each order in orders to ensure that the keys of "amount" and "status", and their corresponding values in the order can be easily and smoothly accessed. 

6. Orders with missing keys: The function checks the "amount" and "status" keys in each order of orders. 

7. Case-insensitive status (order["status"]): The status (order["status"]) is converted to lowercase before comparing it with "cancelled" or "canceled". Through this mechanism, we can handle all orders with cancelled/canceled status in a case-insensitive manner. 

8. Too large datasets: We need to ensure that the function does not crash with large datasets, like orders parameter with 100000 orders inside. 

9. Too large amount (status["amount"]) values: We need to ensure that the function does not crash with too large amount values, like 99999999.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation should mention that the function divides by the number of non-cancelled (valid) orders, not the total number of orders which includes the non-cancelled ones as well.

- The explanation should mention that the function safely handles a non-iterable, empty, or None-type input parameter by returning 0.0. For the empty input parameters (orders), doing this will avoid divide-by-zero errors and thus prevent function from crashing due to them. 

- The explanation should state that the input parameter 'orders' is an iterable, each order in orders is a dictionary-type, each amount in order is a finite and numeric value, and each status in order is a string-type. 

- The explanation should highlight that the function treats "canceled" and "cancelled" in a case-insensitive manner. 

- The explanation should state that the function validates each order in orders, which converts (typecasts) it to a dictionary and skips any non-dict or incompatible/malformed orders.

- The explanation should state that the function converts amount to float, and ignores infinite, NaN (Not-a-Number), invalid, or non-numeric values. 


### Rewritten explanation
> This function calculates the average value of valid orders from the input parameter orders, which should be an iterable of orders. Each order is converted to a dictionary and is expected to contain a numeric, finite amount and a string status.

> The function processes each order by:

> 1: Converting it to a dictionary (skipping any incompatible/malformed orders that cannot be converted).

> 2: Ignoring orders whose status is "cancelled" or "canceled" (case-insensitive).

> 3: Converting amount to a float and including it only if it is numeric and finite.

> The average is computed by dividing the sum of valid amounts by the count of valid orders. If there are no valid orders, the function safely returns 0.0 to avoid division by zero.

## 4) Final Judgment
- Decision: Approve 
- Justification: The function is robust and handles edge cases well, including empty or invalid input, cancelled orders, malformed order data, and non-numeric or infinite amounts, with case-insensitive status checks. The explanation clearly describes the input expectations, orders as an iterable, each order converted to a dictionary, amount numeric and finite, and status a string, and outlines how the function processes and validates them. The average is safely computed by dividing the sum of valid amounts by the count of valid orders, returning 0.0 if there are no valid orders to avoid division by zero error. 

- Confidence & unknowns: Confidence is high because the function has explicit validation steps and type conversions that safely handle most real-world data issues.

Unknowns may include extremely large datasets or very large and finite values of order amounts. We may use yield keyword to process very large iterable of orders one-by-one, and Python's decimal library to handle very large and finite values of amount.   

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- Extremely Inadequate and Loose Email Validation: This code defines a valid email as any string that contains the @ symbol, regardless of its position. After the last '@' symbol, a valid email must have a top-level domain like '.com', and a domain like 'gmail'. This code does not find the last '@' symbol in the email, and it does not check for the presence of any characters following the '@' symbol, including a dot ('.'), a domain like '.gmail', and a top-level domain like '.com'. This will lead to significant amount of "false positives". For instance, using this logic, the following emails would be counted as valid emails: 

"I am @ at work"
"cats@and@dogs"
"@@abc@"
"ahmet123@"

- Handling of Edge Cases: The ai-generated explanation claims that it "safely ignores invalid entries,"; however, this is misleading. If the input iterable (e.g. a list) contains non-string objects (such as integers, floats, lists, or None), the line 'if "@" in email' will raise a TypeError, which causes the entire function to crash.

### Edge cases & risks
The current implementation relies on a single @ check, which introduces several edge cases and risks:

- Missing Domain and Top-Level Domain (TLD) Validation: The current implementation of the function does not find the last '@' symbol in the email. Moreover, it does not verify the presence of a dot (.), a domain like 'gmail', and a top-level domain like '.com', which follow the last '@' symbol found. This means that using the current implementation, the email strings such as 'hello@dad', "@@", "@  b@c", "@monkey", and "myuser@" would be erroneously counted as valid.

- Type Safety Risk of Each Email in Emails: If the emails iterable (e.g. a list) contains non-string data types (e.g., [943, ["da@b.com"], None]), the line 'if "@" in email' will raise a TypeError, and crash the program.

- Type Safety Risk of Emails Input Parameter: The current implementation of the function does not validate the 'emails' parameter. It should not be None or empty, and it should be an iterable such as list, tuple, and set. We should add these checks in order to properly handle incompatible/malformed 'emails' input parameter.


### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- 

### Edge cases & risks
- 

### Code quality / design issues
- 

## 2) Proposed Fixes / Improvements
### Summary of changes
- 

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- 

### Rewritten explanation
- 

## 4) Final Judgment
- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
