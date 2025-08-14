import requests


def encrypt(data):
    url = "https://AntCrypt.whiteant.repl.co/antcrypt/v1/en"
    x = requests.post(url, data=data, timeout=60)
    return str(x.text)


def decrypt(data):
    url = "https://AntCrypt.whiteant.repl.co/antcrypt/v1/dec"
    x = requests.post(url, data=data, timeout=60)
    return str(x.text)

