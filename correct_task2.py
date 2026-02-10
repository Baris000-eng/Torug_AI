# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

import re

EMAIL_REGEX = re.compile(r"^[a-z0-9](?!.*\.{2})[a-z0-9.]{3,33}[a-z0-9]@[a-zA-Z0-9.-]{2,30}+\.[a-zA-Z]{2,20}$")

def is_valid_email(email: str) -> bool:

    return isinstance(email, str) and bool(EMAIL_REGEX.fullmatch(email))


def count_valid_emails(emails):

    if not emails or not isinstance(emails, (list, tuple, set)):
        return 0

    valid_email_count = 0

    for email in list(emails):
        if is_valid_email(email):
            valid_email_count += 1

    return valid_email_count




# print(is_valid_email("bkaplan18@ku.edu.tr"))
# print(is_valid_email("@123.com"))