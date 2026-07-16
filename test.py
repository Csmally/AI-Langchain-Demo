import requests

proxies = {
    "http": "http://127.0.0.1:8899",
    "https": "http://127.0.0.1:8899",
}

requests.get(
    "http://httpbin.org/get",
    proxies=proxies
)