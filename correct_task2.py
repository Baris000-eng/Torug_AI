# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re 

EMAIL_REGEX = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"

def count_valid_emails(emails):

    if not emails or (not isinstance(emails, (list, tuple, set))):
        return 0

    valid_email_count = 0
    for email in emails:
        if isinstance(email, str) and EMAIL_REGEX.fullmatch(email):
            valid_email_count += 1

    return valid_email_count