
from instascrape import *

# session_id = "4245610670:0ABDxaO6Nrf3Be:17:AYdDBi66z13hOtWHJwu-yodkeBFmpJ48KWKH8RrN1Q"  # Replace with your Instagram session ID
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
#     "cookie": f"sessionid={session_id};",}

profile = Profile('https://www.instagram.com/byvfx/')

profile.scrape()

print(profile.followers)
print(profile.following)
