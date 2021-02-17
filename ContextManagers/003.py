from contextlib import contextmanager
import requests

@contextmanager
def context(url):
    req = requests.get(url)
    yield req
    req.close()

with context('https://github.com/') as r:
    print(r.url)
    print(r.headers)
    print(r.cookies)
