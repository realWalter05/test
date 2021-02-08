from flask import Flask
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
s = requests.session()


def send_payload(from_url, to_url, data_payload):
    s.post(from_url, data=data_payload)
    page = s.get(to_url)

    if not page.ok:
        print(f"Payload {from_url} to {to_url} error! Status code of page: {page.status_code}")
    return page


@app.route('/')
def index():
    payload = {
        "username": "zikav29z",
        "password": "1c2zkH51",
        "returnUrl": "/dashboard",
        "login": "",
    }
    page_komens = send_payload("https://zsebenese.bakalari.cz/Login", "https://zsebenese.bakalari.cz/next/komens.aspx?s=rok",
                               payload)
    bs = BeautifulSoup(page_komens.content, 'html.parser')
    return "<h1>Welcome to our server !!</h1>" + bs.getText()
