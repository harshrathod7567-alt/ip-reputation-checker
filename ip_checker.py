import requests
from config import API_KEY

def check_ip(ip_address):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": API_KEY,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    return data["data"]

ip = "8.8.8.8"  # Google's public DNS, safe test IP
result = check_ip(ip)

print(f"IP: {result['ipAddress']}")
print(f"Abuse Confidence Score: {result['abuseConfidenceScore']}%")
print(f"Country: {result.get('countryCode', 'Unknown')}")
print(f"Total Reports: {result['totalReports']}")
print(f"Is Public: {result['isPublic']}")
