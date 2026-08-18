# IP Reputation Checker

A beginner Python project that checks IP addresses against AbuseIPDB's threat 
intelligence database to assess risk level — a real technique used in SOC triage.

## What it does
- Queries the AbuseIPDB API for one or more IP addresses
- Retrieves an "abuse confidence score" (0-100%) based on community-reported malicious activity
- Classifies each IP as LOW, MEDIUM, or HIGH risk
- Saves results to a report file

## Files
- `ip_checker.py` — the main script
- `config.py` — stores your API key (NOT included in this repo — see setup below)
- `.gitignore` — ensures config.py is never accidentally committed

## Setup
1. Sign up for a free API key at [abuseipdb.com](https://www.abuseipdb.com)
2. Create a `config.py` file in this folder with: `API_KEY = "your_key_here"`
3. Install dependencies: `pip install requests`

## How to run it
1. Edit the `ips_to_check` list in `ip_checker.py` with the IPs you want to check
2. Run: `python ip_checker.py`
3. Check the terminal output and `ip_report.txt` for results

## Example output
IP: 8.8.8.8
Risk: LOW RISK (score: 0%)
Country: US
Reports: 0


## What I learned
- Working with real-world threat intelligence APIs
- Proper handling of API keys (never commit secrets to a public repo!)
- Classifying risk levels based on quantitative scores, a real SOC triage technique

## Next steps
- Add domain reputation checking (not just IPs)
- Batch-check IPs from an actual log file (tie this into the log analyzer project!)
- Add rate-limit handling for the free API tier
- 
