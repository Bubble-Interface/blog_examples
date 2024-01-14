import time
from functools import wraps

def retry(max_retries, delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    response = func(*args, **kwargs)

                    if 200 <= response.status_code < 300:
                        return response
                    else:
                        raise Exception(f"Request failed with status code: {response.status_code}")

                except Exception as e:
                    print(f"Attempt {attempts + 1} failed: {e}")
                    time.sleep(delay)
                    attempts += 1

            print(f"Maximum retries reached for function: {func.__name__}")
            return None

        return wrapper

    return decorator
