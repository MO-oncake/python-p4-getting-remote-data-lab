import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request to the URL and return the response body as bytes
        response = requests.get(self.url)
        return response.content  # Use .content to get the raw byte response

    def load_json(self):
        # Use get_response_body to get the raw response and parse it as JSON
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))  # Decode bytes to string and parse as JSON
