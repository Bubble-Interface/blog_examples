from utils import make_api_get_request

def main():
    result = make_api_get_request('https://example.com/api/data')
    if result:
        print("API request successful:", result.json())
    else:
        print("API request failed.")


if __name__ == "__main__":
    main()