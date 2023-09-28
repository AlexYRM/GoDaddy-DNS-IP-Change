import read
import requests
from config import config


# Define headers for GoDaddy API authentication
headers = {
    "Authorization": f"sso-key {config.key}:{config.secret}"
}


def check_current_ip():
    # Define the API endpoint and make a GET request
    url = f"https://api.godaddy.com/v1/domains/{config.domain}/records/A/{config.name}"
    response = requests.get(url, headers=headers)
    # Transform the response in a dict
    data = response.json()
    # Extract the current IP address from the API response
    current_ip = data[0]["data"]
    print(current_ip)
    return current_ip


def update_ip(ip, func_ttl, func_name):
    func_url = f"https://api.godaddy.com/v1/domains/{config.domain}/records/A/{func_name}"
    print(func_url)
    # Define the data payload for the PUT request
    data = [
        {
            "data": ip,
            "port": 1,
            "priority": 0,
            "protocol": "string",
            "service": "string",
            "ttl": func_ttl
        }
    ]
    # Send the PUT request to update the DNS record
    requests.put(func_url, headers=headers, json=data)


def ip_verification():
    # Get the server's current IP address
    server_ip = read.server_ip()
    # Get the current IP address associated with the DNS record
    website_ip = check_current_ip()
    # Compare the two IP addresses and update if different
    if website_ip != server_ip:
        # Update both primary and secondary DNS records with the new IP address
        update_ip(ip=server_ip, func_name=config.name, func_ttl=config.ttl)
        update_ip(ip=server_ip, func_name=config.ntfy_name, func_ttl=config.ntfy_ttl)
        print("Changed IP")
    else:
        print("IP is the same as the server")
