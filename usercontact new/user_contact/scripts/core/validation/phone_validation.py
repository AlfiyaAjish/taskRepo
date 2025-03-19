# user_contact/scripts/core/validation/phone_validation.py
import re


def is_valid_phone_number(phone_number: str) -> bool:
    """
    Validates a phone number using regex.
    :param phone_number: Phone number string to validate
    :return: True if the phone number is valid, False otherwise
    """
    phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format validation

    if re.match(phone_regex, phone_number):
        return True
    return False
