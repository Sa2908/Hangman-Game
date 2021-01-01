import requests

url = "https://random-word-api.herokuapp.com/word"


def get():
    word = requests.get(url).json()[0]
    return word