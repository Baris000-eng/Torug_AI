# AI Code Review Assignment (Python)

## Candidate
- Name: Barış Kaplan 
- Approximate time spent: 120 minutes (2 hours)

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- The given code assumes that the "status" and "amount" keys are already existing in the dictionary named 'order'. However; if one of these keys is missing in the dictionary 'order', the function will raise a KeyError, regarding the missing key. 

- Irrespective of how many orders are cancelled, we are currently dividing the total order amount by the length (len(orders)) of the orders data structure (e.g. a list). This means that the count of the cancelled orders are still included in the divisor, even though they are excluded from the total order value. So, this will skew and give the wrong average order value at the end. 

- No type validation is performed on the orders, each order in the orders, and the values existing in each order. order["status"] might not be of type string (such as int, float, or None), which will cause error while comparing it with "cancelled". Moreover, order["amount"] can be a None, string, or a non-numeric value. This would cause a ValueError or TypeError. 

- Each order in orders data structure can be a data type other than a dictionary. We need to ensure that each order in orders to be a dictionary. 


### Edge cases & risks
- For the empty input parameter of orders (such as list(), [], and tuple()), the count will be zero. Therefore, while calculating the average order value (total / count), the current version of the code will throw a divide-by-zero error. 

- Orders data structure can be empty or None, or it can be a data type other than the list, tuple, or set. These cases are not handled in the current version of the code. 

- Order amounts with infinite values are included in the current version, which will skew the average order value calculation. 

- Order status check is done in a case-sensitive manner. One can type the order status value as "CANcelled". It will also mean that the order is cancelled and we need to do this check in a case-insensitive manner. If not, then we will skip such values of the order statuses, which will lead to a wrong average order value.



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
the valid_count is incremented only if the order is non-cancelled. An if statement checking whether the valid_count is 0 is added after the for loop. If so, we return 0.0 as the average. Through this if check, we can handle empty orders parameter (e.g. [] or list()) without any errors. 

- Input parameter validation is added: It checks if order is not a list/tuple/set, or is empty, and return 0.0 as the average order value if so. 

- Case insensitive order status comparison: Conversion of order["status"] to lowercase, before comparing it with the "cancelled", is added. This string value could be given as "cancelled" or "canceled". The "canceled" is preferred in the American English, and the "cancelled" is preferred in the British English. So, both of these versions are correct. 

- Safer key access is added: Verification of the existence of both the "status" and "amount" keys is added before using them. 

- Amount validation is improved: The amount (status["amount"]) is converted to float using the 
float() function within a try-except block. This will ensure that the amount is either a float or an integer. This conversion in the try-except block ensures that any amount values of incompatible types are safely ignored. Moreover, math.isfinite(amount) is used to ignore infinite or NaN values of the amount. 

- More robust order data handling is added: Each order in orders is safely typecasted/converted into a dictionary (dict()) within a try-except block. Each order that is not a dictionary type  (e.g. an integer) is handled and skipped. 

- Error tolerance is added: Risky operations like typecasting (e.g. float() and dict()) are wrapped with try-except blocks so that the bad data does not crash the function. 


### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?

1. True-structured orders parameter with true-structured dictionaries where correct keys and correct type of values are located in each dictionary: 

I will initially test the case where the orders parameter, each order in orders, and the keys and values in each order are correctly structured and typed. Because,
our function should work seamlessly where the parameter is fully as expected.

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
- Extremely Inadequate and Loose Email Validation: This code defines a valid email as any string that contains the @ symbol, regardless of its position. After the last '@' symbol, a valid email must have a top-level domain like '.com', and a domain like 'gmail'. This code does not find the last '@' symbol in the email, and it does not check for the presence of any characters following the '@' symbol, including a domain like 'gmail', a dot ('.'), and a top-level domain like 'com'. This will lead to significant amount of "false positives". For instance, using this logic, the following emails would be counted as valid emails: 

"I am @ at work"
"cats@and@dogs"
"@@abc@"
"ahmet123@"

- Handling of Edge Cases: The ai-generated explanation claims that it "safely ignores invalid entries,"; however, this is misleading. If the input iterable (e.g. a list) contains non-string objects (such as integers, floats, lists, or None), the line 'if "@" in email' will raise a TypeError, which causes the entire function to crash.

### Edge cases & risks
The current implementation relies on a single @ check, which introduces several edge cases and risks:

- Type Safety Risk of Each Email in Emails: If the emails iterable (e.g. a list) contains non-string data types (e.g., [943, ["da@b.com"], None]), the line 'if "@" in email' will raise a TypeError, and crash the program.

- Type Safety Risk of 'Emails' Input Parameter: The current implementation of the function does not validate the 'emails' parameter. It should not be None or empty, and it should be an iterable such as list, tuple, and set. We should add these checks in order to properly handle incompatible/malformed 'emails' input parameter.


### Code quality / design issues
1. Logic & Validation Issues

    - Missing Standards: The current code does not check the existence of a domain (like 'gmail'), a dot (.), and a top-level domain (like 'com'), following the last '@' symbol found in the email in sequence.

    - False Positives: The strings "@pear", "me@" and "@@@@"  would be counted as valid emails, although they are not real email addresses.

    - Type Safety Checks on Each Email: Each email in emails should be a string. To ensure this, we need to add a type safety check in our current code for each email. 

    - Missing Character Checks: The current code does not check whether invalid characters such as whitespace, special characters, and punctuation marks exist in the email. Moreover, it does not check whether alphanumerical characters exist in the email. These checks should be added to the current implementation to ensure that we have valid emails and that only they are counted.  

    - Type Safety Risk of 'Emails' Input Parameter: The current implementation of the function does not validate the 'emails' parameter. It should be checked to ensure that it is not None and it is a non-empty iterable such as list, tuple, and set. These checks should be added in order to properly handle incompatible/malformed 'emails' input parameter. 
    
2. Code Maintainability Issue: 
    - The email validity logic is currently handled directly inside the count_valid_emails() function, which makes the function harder to read, test, and maintain. The email validation logic should be extracted into a separate helper function (e.g., is_valid_email()), and then called within count_valid_emails(). This separation would improve readability, promote reusability, simplify testing, and make future changes to the validation rules easier to manage.



## 2) Proposed Fixes / Improvements
### Summary of changes
- I replaced the simple 'if "@" in email' check with a robust regex-based (EMAIL_REGEX) check to ensure the email follows a 
proper structure (user, domain, and top-level domain) with appropriate type and amount of characters in each part. 

The email regex that I have added: 

EMAIL_REGEX = re.compile(r"^[a-z0-9](?!.*\.{2})[a-z0-9.]{3,33}[a-z0-9]@[a-zA-Z0-9.-]{2,30}+\.[a-zA-Z]{2,20}$")

What does this email regex check?: 

* Starts with alphanumeric character: ^[a-z0-9] ensures the email begins with a letter or number, not a special character.

* No consecutive dots: (?!.*\.{2}) is a negative lookahead that ensures I do not allow two or more dots 
in a row (e.g., myuser123....name@example.com is invalid).

* Username length and content: [a-z0-9.]{3,33} allows letters, numbers, and dots for the username, restricting the total 
length to be between 3 and 33 characters.

* Ends username with an alphanumeric character: [a-z0-9] ensures the username part does not end with a dot.

* Domain structure: @[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ensures the email has a @symbol, followed by a domain name (alphanumeric, hyphens, dots), 
and ends with a top-level domain (like .comor .org) that is at least 2 characters long.

- I added checks to ensure the input is actually a list, tuple, or set, and I handle empty/None inputs properly with 'if not emails'.

- I created a dedicated helper function is_valid_email() with the email parameter to make the code cleaner, more readable, 
easier to test, and easier to change. In this helper function, I added the 'isinstance(email, str)' check to ensure the code does not crash if 
a non-string object is passed in the list. I have used a full match check with the provided email regex, 'bool(EMAIL_REGEX.fullmatch(email))', to 
ensure that the provided email is fully matching with the email format given in the email regex, and no extra text is allowed before or 
after the valid structure . This guarantees that a string like "user@example.comextratexthere" is correctly identified as invalid.
Moreover, I have called this function for each email in emails. If the email is valid, I have incremented the valid email counter by one. 


### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

I would focus on the following test areas/scenarios: 

 Valid Email Formats: I would test standard, valid emails to ensure the regex pattern allows them.

    * Examples: testuser@example.com , user.name+tag@sub.domain.co.uk.

  Malformed Email Structure: I would test different email structures that violate the EMAIL_REGEX to ensure they are correctly ignored.

    * Examples: Missing @, missing domain, missing top-level domain, an email with a username less than 5 or more than 35 charachters, 
    an email with a username ending with dot, email with a username containing consecutive dots, email with a domain name containing 1 
    charachter or more than 30 charachters, an email with a top-level domain containing 1 charachter or more than 20 charachter, an email 
    containing alphanumerical charachters in its username but not in its domain name or extension, and so forth.


 Username and Domain Constraints: I would verify the length restrictions and character constraints I set in the regex.

    * Examples: Usernames that are too short/long, or domains with invalid characters.

 Consecutive Dot Constraint: Specifically, I would test for double dots within the username to ensure the negative lookahead ( (?!.*\.{2})) functions correctly.

    * Examples: user..name@example.com .

 Extra Text/Whitespace ( fullmatchverification): I would test strings that contain a valid email pattern but have additional text or spaces around it to confirm fullmatch() rejects them.

    * Examples: "user@example.comextra_text", " user@example.com".

 Input Type Handling: I would test the function with incorrect data types for the emails argument to ensure it handles them without crashing.

    * Examples: Passing a single string instead of a list, or passing None.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- It is inaccurate : The explanation claims it counts "valid" email addresses, but the code only checks whether the character "@" exists in the string. However, this 
does not consider the position of the '@' symbol within the email. The current code does not validate how many and what type of characters can be located in which part 
of the email. Moreover, it does not validate if the email has a username, a domain like 'gmail', and a proper extension (Top-Level Domain (TLD)) like 'com'. 

- It fails to describe the logic : It does not mention that the validation is limited strictly to a substring check, rather than a structural regex validation.

- It is overly optimistic : It states the function "safely ignores invalid entries". However, if a user passes a string like "invalid-email" or "@", the code incorrectly 
counts them as valid simply because they contain an '@' symbol.

- No description about the data type of each email: It does not explicitly mention that each email within the emails needs to be a string for the validation logic to work correctly. 

### Rewritten explanation
> This function accurately counts valid email addresses and handles empty emails input correctly by implementing strict validation rules based on a robust regular expression.

> Input Validation: The function checks if the input parameter emails is a valid iterable structure (list, tuple, or set) and handles empty or non-iterable inputs by returning a count of 0 immediately.

> Strict String Validation: A dedicated helper function is_valid_email is used with re.fullmatch to enforce the following rules defined in the EMAIL_REGEX:

* Starts with alphanumeric: The username must begin with a letter or number.

* No consecutive dots: The username cannot contain consecutive dots like '...'

* Length and Character Constraints: The username must contain between 3 and 33 characters (letters, numbers, or dots) between the first 
and last characters. Therefore, the total username length must be between 5 and 35 characters.

* Ends with alphanumeric: The username must end with a letter or number, not a dot.

* Domain Structure: After the username ends, an '@' symbol should come. Then, a valid @ symbol must be followed by a domain name and a top-level 
domain (such as '.com', and '.org') that is at least 2 characters long.

> Error Handling: The function (specifically is_valid_email(email)) verifies that each item is a string (isinstance(email, str)) before validation, 
> ensuring non-string items within the input list are safely ignored and the function does not crash.

## 4) Final Judgment
- Decision: Approve 

- Justification: It was approved because it successfully transitioned from a simplistic substring check ('@' in email) to a robust, regex-based validation. 
It correctly handles various input data types (lists, tuples, sets), ensures only strings are processed to prevent runtime errors, and enforces strict structural 
rules for email addresses. Moreover, the updated implementation correctly handles the empty input, and safely ignores 
the invalid entries (such as non-iterable emails, None emails, and non-string email in the emails list). 

- Confidence & unknowns: There is a high confidence. There are no notable unknowns regarding the code logic or the requirements of the explanation.

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
