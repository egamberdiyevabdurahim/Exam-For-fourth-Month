from data import email_details, phone_details


def validate_email(email: str):
    """
    Check if email is valid.
    """
    message: bool = False
    if email.endswith(email_details):
        message: bool = True
    return message


def validate_phone(phone: str):
    """
    Check if phone number is valid.
    """
    message: bool = False
    if len(phone) == 9 and phone.isdigit() and phone[:2] in phone_details:
        message: bool = True
    return message


def validate_gender(gender: str):
    """
    Check if gender is valid.
    """
    message: bool = False
    if gender.lower() not in ["m", "f"]:
        message: bool = True
    return message
