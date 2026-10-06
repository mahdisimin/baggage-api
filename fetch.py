import requests

def fetch_data():
    res = requests.get("https://httpbin.org/get",timeout=(5,1))
    print(res.text)
    print(res.headers)


if __name__ == '__main__':
    fetch_data()