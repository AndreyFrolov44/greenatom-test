import requests
from bs4 import BeautifulSoup


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def get_html() -> str:
    return requests.get('https://ifconfig.me/', headers=headers).text


def get_ip() -> str:
    soup = BeautifulSoup(get_html(), 'html.parser')
    ip = soup.find(id='ip_address').text
    return ip


print(get_ip())
