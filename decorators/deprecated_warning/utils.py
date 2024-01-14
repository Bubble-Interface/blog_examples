import re
import socket

from deprecated_warning_decorator import deprecated

@deprecated
def validate_email_old(email):
    """
    Deprecated function for validating email addresses.
    
    It is recommended to use the updated function `validate_email` for 
    additional domain validation
    
    Parameters:
    - email (str): The email address to be validated.
    
    Returns:
    - bool: True if the email is valid, False otherwise.
    """

    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(pattern.match(email))


def validate_email(email):
    """
    Updated function for comprehensive email validation.
    
    Additional domain validation on top of basic email validation
    using a regular expression pattern
    
    Parameters:
    - email (str): The email address to be validated.
    
    Returns:
    - bool: True if the email is valid, False otherwise.
    """

    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    if not pattern.match(email):
        return False

    domain = email.split('@')[1]

    try:
        socket.gethostbyname(domain)
    except socket.gaierror as e:
        print(f'Domain name resolution for {domain}: {e}')
        return False 

    return True

