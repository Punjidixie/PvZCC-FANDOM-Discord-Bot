import requests


def get_json(url_segment):
    f = open("url.txt", "r")
    fandom_url = f.read()
    f.close()
    
    response = requests.get(fandom_url + "/" + url_segment)
    return response.json()
    