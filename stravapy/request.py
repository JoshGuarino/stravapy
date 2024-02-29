import requests

class Request(object):
    def get(headers: dict, url: str):
        try:
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                return response
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def post(headers: dict, url: str):
        try:
            response = requests.get(url=url, headers=headers)
            if response.status_code == 201:
                return response
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def put(headers: dict, url: str):
        try:
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                return response
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)