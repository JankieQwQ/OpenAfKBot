import urllib.request

def random_picture() -> object:
    API = 'http://www.98qy.com/sjbz/api.php'
    return urllib.request.urlopen(API).read()