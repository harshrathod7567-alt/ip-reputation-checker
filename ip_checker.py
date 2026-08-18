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

def check_multiple_ips(ip_list):
    results = []
    for ip in ip_list:
        try:
            result = check_ip(ip)
            score = result["abuseConfidenceScore"]
            
            if score >= 75:
                risk = "HIGH RISK"
            elif score >= 25:
                risk = "MEDIUM RISK"
            else:
                risk = "LOW RISK"
            
            results.append({
                "ip": result["ipAddress"],
                "score": score,
                "risk": risk,
                "country": result.get("countryCode", "Unknown"),
                "reports": result["totalReports"]
            })
        except Exception as e:
            results.append({"ip": ip, "error": str(e)})
    
    return results

# Test with a few IPs (mix of safe and known-flagged test IPs)
ips_to_check = ["8.8.8.8", "1.1.1.1"]

results = check_multiple_ips(ips_to_check)

print("=== IP Reputation Check ===\n")
for r in results:
    if "error" in r:
        print(f"{r['ip']}: ERROR - {r['error']}")
    else:
        print(f"IP: {r['ip']}")
        print(f"  Risk: {r['risk']} (score: {r['score']}%)")
        print(f"  Country: {r['country']}")
        print(f"  Reports: {r['reports']}")
        print()
