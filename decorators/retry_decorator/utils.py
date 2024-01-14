import requests

from retry_decorator import retry

@retry(max_retries=3, delay=1)
def make_api_get_request(url):
    """
    Make a GET request to the specified API endpoint.

    Parameters:
    - url (str): The URL of the API endpoint to send the GET request to.

    Returns:
    - requests.Response: The response object containing the result of the API request.
    """
    response = requests.get(url)
    return response
