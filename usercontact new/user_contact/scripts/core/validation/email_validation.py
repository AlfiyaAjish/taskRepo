import re
def is_valid_email(email: str) -> bool:
    """
    Validates an email address using regex.
    :param email: Email string to validate
    :return: True if the email is valid, False otherwise
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(email_regex, email):
        return True
    return False
