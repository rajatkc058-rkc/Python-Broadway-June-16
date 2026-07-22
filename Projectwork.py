import requests
import json
import time
import  csv
viber_token = '56dbfd241d322b4f-47b755db63e2c85f-6d281e62d622c54a'
user_id = "nffEXekaqSrbdtm2n2kkrQ=="
viber_url = "https://chatapi.viber.com/pa/post"
Pl_url ="https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2026/teams?pageSize=100"
image_url = "https://resources.premierleague.com/premierleague25/badges-alt/43.png"

# def send_message_viber(message,image):
    # payload = {  
#    "auth_token":viber_token, 
#    "from":user_id, 
#    "type":"picture", 
#    "text":message,
#    "media":image, 
#    "thumbnail":image 
# } 
    # r = requests.post(url = viber_url,data = json.dumps(payload))
with open('premier_league_teams.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Message', 'Image URL'])
    r = requests.get(url= Pl_url)
    if r.status_code == 200:
        viber = r.json()
        result = viber['data']
        for i in result:
            message = f"{i['name']}{i['abbr']} Football Club plays their home matches at the {i['stadium']['name']} in {i['stadium']['city']}, {i['stadium']['country']}, which has a seating capacity of {i['stadium']['capacity']}."
            # print(message)
            image = f"https://resources.premierleague.com/premierleague25/badges-alt/{i['id']}.png"
            # print(image)
            # send_message_viber(message, image)
            writer.writerow([message, image])
            # time.sleep(0.5)        
    else:
            print("api error")
