import requests
import json
import time
import  mysql.connector

viber_token = '56dbfd241d322b4f-47b755db63e2c85f-6d281e62d622c54a'
user_id = "nffEXekaqSrbdtm2n2kkrQ=="
viber_url = "https://chatapi.viber.com/pa/post"
Pl_url ="https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2026/teams?pageSize=100"
image_url = "https://resources.premierleague.com/premierleague25/badges-alt/43.png"

db = mysql.connector.connect(
    host="localhost", user="root", port=3306, database="games"
)
terminal = db.cursor()
query = """create table IF NOT Exists Teams (Id int Primary Key Auto_Increment,
team_name VARCHAR(255),
abbr VARCHAR(10),
stadium_name VARCHAR(255),
city VARCHAR(100),
country VARCHAR(100),
capacity INT,
image_url TEXT
);"""
terminal.execute(query)
db.commit()


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
try:
    r = requests.get(url=Pl_url)
    if r.status_code == 200:
        viber = r.json()
        result = viber['data']
        for i in result:
            name = i['name']
            abbr = i['abbr']
            st_name = i['stadium']['name']
            city = i['stadium']['city']
            country = i['stadium']['country']
            capacity = i['stadium']['capacity']
            image = f"https://resources.premierleague.com/premierleague25/badges-alt/{i['id']}.png"
            query = f"Insert into Teams (team_name,abbr,stadium_name,city,country,capacity,image_url) values('{name}','{abbr}','{st_name}','{city}','{country}','{capacity}','{image}')"
            terminal.execute(query)
        db.commit()
        # send_message_viber(message, image)
        # time.sleep(0.5)     
    else:
        print("api error")
except Exception as e:
        print("Error:",e)
