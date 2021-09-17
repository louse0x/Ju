import requests

url = "https://api.promptapi.com/dns_lookup/api/any/tjhzyl.com"

payload = {}
headers= {
  "apikey": "BZGEIOrmVkrDBZH9AdTyHE1yKeQnJ0DE"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response

print(result)