import os
from pathlib import Path

from utils import validate_email_old, validate_email

def main():
    email = "user@nonexistingdomain.com"
    
    # Example usage of the deprecated function
    result_old = validate_email_old(email)
    print(f"Old Email Validation Result for {email}: {result_old}")
    
    # Example usage of the updated function
    result_new = validate_email(email)
    print(f"Updated Email Validation Result for {email}: {result_new}")


if __name__ == "__main__":
    main()