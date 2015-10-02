import http.client
import json


class Storage:
    @staticmethod
    def store(content):
        body = {
            "description": "Got from stdin :)",
            "public": True,
            "files": {
                "ShellOutput.txt": {
                    "content": content
                }
            }
        }

        connection = http.client.HTTPSConnection('api.github.com')

        try:
            connection.request('POST', '/gists', json.dumps(body), {
                "application": "vnd.github.VERSION.raw+json",
                "Content-Type": "application/json",
                "User-Agent": "app"
            })
        except Exception as e:
            print(e)

        response = connection.getresponse()
        response_json = json.loads(response.read().decode('UTF-8'))

        return response_json['html_url']
