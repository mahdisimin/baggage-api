import requests

def fetch_data() -> str:
    res = requests.get("https://httpbin.org/get", timeout=(1, 5))
    txt = (res.text)
    print(res.headers)
    return txt


if __name__ == "__main__":
    txt = fetch_data()
    print(txt)
