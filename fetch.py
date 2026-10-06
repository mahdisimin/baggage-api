import requests

def fetch_data():
    res = requests.get("https://httpbin.org/delay/2", timeout=(1, 5))
    print(res.text)
    print(res.headers)


if __name__ == "__main__":
    fetch_data()
