import requests

class Request(object):
    def get(url: str, headers: dict):
        try:
            return requests.get(url=url, headers=headers)
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def post(url: str, headers: dict):
        try:
            return requests.post(url=url, headers=headers)
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def put(url: str, headers: dict):
        try:
            return requests.put(url=url, headers=headers)
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)