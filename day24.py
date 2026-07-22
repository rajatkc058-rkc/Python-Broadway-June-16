# # viber_token = '56dbfd241d322b4f-47b755db63e2c85f-6d281e62d622c54a'
# # user_id = "nffEXekaqSrbdtm2n2kkrQ=="

# import requests
# import json

# reqUrl = "https://chatapi.viber.com/pa/post"

# headersList = {
#  "Accept": "*/*",
#  "User-Agent": "Thunder Client (https://www.thunderclient.com)",
#  "Content-Type": "application/json" 
# }

# payload = json.dumps({
#    "auth_token":"56dbfd241d322b4f-47b755db63e2c85f-6d281e62d622c54a",
#     "from":"nffEXekaqSrbdtm2n2kkrQ==", 
#     "type":"text", 
#     "text":"Good morning form my home KC niwas" 
# })

# response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

# print(response.text)