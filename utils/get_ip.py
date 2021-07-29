import requests

def get_ip():
    res = requests.get('https://ident.me/')
    return str(res.content.decode('utf-8'))
