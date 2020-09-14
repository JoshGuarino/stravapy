import requests

class Request(object):
    def get(headers, url):
        try:
            response = request.get(url=url, headers=headers)
            if response.status_code == 200:
                return response
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def post(headers, url):
        try:
            response = request.get(url=url, headers=headers)
            if response.status_code == 201:
                return response
        except requests.exceptions.HTTPError as error:
            raise SystemExit(error)

    def test():
        print('test2')
        return 