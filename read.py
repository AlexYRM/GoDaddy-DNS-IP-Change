import re
import requests
from config import config
from bs4 import BeautifulSoup


def server_ip():
    # Send an HTTP GET request to the server URL using the provided headers
    response = requests.get(config.server_url, headers=config.server_header)
    # Create a BeautifulSoup object to parse the HTML content of the response
    soup = BeautifulSoup(response.text, "html.parser")
    # Use regular expressions to find all IP addresses (IPv4) in the HTML content
    ip = re.findall(r"\d+\.\d+\.\d+\.\d+", soup.text)

    print(f"Tere server IP is {ip[0]}")
    # Return the first IP address found
    return ip[0]
