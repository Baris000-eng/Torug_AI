# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

"""
Compiled regular expression object for validating email addresses.

Validation Rules:
- Starts and ends with alphanumeric characters.
- Contains alphanumeric characters, dots (.), underscores (_), or hyphens (-).
- No consecutive dots (..) allowed.
- Domain and top-level domain parts should be valid.
- Length restrictions applied to local part and domain. Each username part must
be between 5 and 35 characters, the domain part must be between 2 and 30 characters, 
and the top-level domain must be between 2 and 20 characters. 
"""

# Email Validation Regex: Defines the pattern for a structurally sound email address.
EMAIL_REGEX = re.compile(
    r"^[a-zA-Z0-9](?!.*\.{2})[a-zA-Z0-9._-]{3,33}[a-zA-Z0-9]"  # Username part with length restrictions and no consecutive dots 
    r"@"                                                       # The '@' symbol seperating the username and domain
    r"[a-zA-Z0-9](?!.*\.{2})[a-zA-Z0-9.-]{0,28}[a-zA-Z0-9]"    # Domain part with length restrictions and no consecutive dots 
    r"\.[a-zA-Z]{2,20}$"                                       # Extension part (Top-Level Domain (TLD)) with length restrictions
, re.VERBOSE)

def is_valid_email(email: str) -> bool:
    """
    Checks if a string is a valid email address based on predefined regex rules.

    Args:
        email: The string to be validated.

    Returns:
        True if the email format is valid, False otherwise (or if input is not a string).

    Example:
        > is_valid_email("myuser@example.com")
        True
        
        > is_valid_email("invalid-email-example")
        False
    """
    # Input Type Validation: Ensure input is a string before regex matching.
    # Pattern Matching: Use fullmatch to check if the entire string matches the pattern.

    return isinstance(email, str) and bool(EMAIL_REGEX.fullmatch(email))


def validate_emails(emails): 
    """It validates a collection of email addresses. It ensures that 
    the emails input is a non-empty/non-None iterable (list, tuple, set)"""
    # Input Validation: Check if input is empty, None, or not an allowed iterable type.
    if not emails or not isinstance(emails, (list, tuple, set)):
        return False 
    return True 

def count_valid_emails(emails):
    """
    Counts the number of valid email addresses within a collection.

    This function iterates through an iterable (list, tuple, set), filters out
    non-string types, and checks each string against the validation rules
    defined in `is_valid_email`. It hanndles various edge cases seamlessly,
    such as empty/None inputs, non-iterable inputs, and collections with 
    malformed, missing, non-string, and/or incompatible data. 

    Args:
        emails: An iterable containing email addresses (strings) to check.

    Returns:
        The total count of valid email addresses. Returns **0** if the input
        is empty, not a valid iterable type, or contains no valid emails.

    Example:
        > email_list = ["test@test.com", "invalid", 123, "info@company.co"]
        > count_valid_emails(email_list)
        2
    """
    if validate_emails(emails) == False:
        return 0

    valid_email_count = 0

    # Iteration: Loop through the provided collection of emails.
    for email in emails:
        # Content Validation: Check if the current item is a valid email string.
        if is_valid_email(email):
            valid_email_count += 1
        else:
            # Skip invalid email entries (non-string, incompatible types, or malformed strings)
            continue

    # Result: Return the total count of valid emails found.
    return valid_email_count




# print(is_valid_email("bariskaplan2000@gmail.com"))
# print(is_valid_email("bkaplan18@ku.edu.tr"))
# print(is_valid_email("@@@123.com"))