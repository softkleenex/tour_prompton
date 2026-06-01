import os
import urllib.request
import urllib.parse
import json

# Try to load env variables manually from .env file
env_path = ".env"
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key, val = line.strip().split("=", 1)
                os.environ[key] = val

api_key = os.environ.get("TOUR_API_KEY")

if not api_key:
    print("ERROR: TOUR_API_KEY is not set!")
    exit(1)

url = "http://apis.data.go.kr/B551011/KorService1/areaBasedList1"

# We will test two methods of passing the serviceKey
# Method 1: Using urllib.parse.urlencode (which URL-encodes the key)
# Method 2: Appending the raw key string directly to the URL (without URL-encoding it)
# Method 3: Unquoting the key first and then appending it raw

methods = [
    {
        "name": "Method 1: URL-encoded Key via urlencode",
        "url_build": lambda key: f"{url}?{urllib.parse.urlencode({'serviceKey': key, 'numOfRows': '3', 'pageNo': '1', 'MobileOS': 'ETC', 'MobileApp': 'AppTest', '_type': 'json'}, safe='~()*')}"
    },
    {
        "name": "Method 2: Raw Key Appended Directly",
        "url_build": lambda key: f"{url}?serviceKey={key}&numOfRows=3&pageNo=1&MobileOS=ETC&MobileApp=AppTest&_type=json"
    },
    {
        "name": "Method 3: Unquoted (Decoded) Raw Key Appended Directly",
        "url_build": lambda key: f"{url}?serviceKey={urllib.parse.unquote(key)}&numOfRows=3&pageNo=1&MobileOS=ETC&MobileApp=AppTest&_type=json"
    }
]

for method in methods:
    print(f"\n--- Testing {method['name']} ---")
    request_url = method["url_build"](api_key)
    
    try:
        req = urllib.request.Request(
            request_url,
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            response_code = response.getcode()
            print(f"HTTP Code: {response_code}")
            raw_data = response.read()
            
            # Print response snippet
            response_text = raw_data.decode('utf-8', errors='ignore')
            print(f"Response: {response_text[:200]}...")
            
            if "response" in response_text or "header" in response_text:
                print("-> SUCCESS! This method returned valid API response structure.")
                # If we got a valid response (even if it lists an error code inside the XML/JSON, we can inspect it)
    except Exception as e:
        print(f"-> FAILED. Error: {e}")
