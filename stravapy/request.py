import requests

class Request:
    def get(self, url: str, headers: dict):
        try:
            return requests.get(url=url, headers=headers)
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def post(self, url: str, headers: dict):
        try:
            return requests.post(url=url, headers=headers)
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def put(self, url: str, headers: dict):
        try:
            return requests.put(url=url, headers=headers)
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)
