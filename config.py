import os
import json
import dotenv
import requests

dotenv.load_dotenv()


class Config:
    def __init__(self):
        self.doppler_token = os.getenv("DOPPLER_TOKEN")
        self.url = "https://api.doppler.com/v3/configs/config/secrets/download?format=json"
        self.domain = ""
        self.name = ""
        self.ntfy_name = ""
        self.ttl = ""
        self.ntfy_ttl = ""
        self.key = ""
        self.secret = ""
        self.server_url = ""
        self.server_header = ""
        self.parsing_data()

    # Function to download secrets from doppler server by sending a get request
    def download_secrets(self, token):
        payload = {}
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.request("GET", self.url, headers=headers, data=payload)
        return response.text

    # Function to download and parse data from the Doppler and store them in the class attributes
    def parsing_data(self):
        # Download secrets using the provided token
        json_data = self.download_secrets(self.doppler_token)
        # Parse the downloaded JSON data
        data = json.loads(json_data)
        # Extract specific values from the parsed JSON data and store them in class attributes
        self.domain = data.get("DOMAIN")
        self.name = data.get("NAME")
        self.ntfy_name = data.get("NTFY_NAME")
        self.ttl = int(data.get("TTL"))
        self.ntfy_ttl = int(data.get("NTFY_TTL"))
        self.key = data.get("KEY")
        self.secret = data.get("SECRET")
        self.server_url = data.get("SERVER_URL")
        self.server_header = json.loads(data.get("SERVER_HEADER").replace("'", "\""))


config = Config()
