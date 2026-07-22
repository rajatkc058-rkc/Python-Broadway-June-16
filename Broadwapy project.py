import requests
import json
import time
import mysql.connector

viber_token = "56dbfd241d322b4f-47b755db63e2c85f-6d281e62d622c54a"
user_id = "nffEXekaqSrbdtm2n2kkrQ=="
viber_url = "https://chatapi.viber.com/pa/post"

Pl_url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2026/teams?pageSize=100"

# image_url = "https://resources.premierleague.com/premierleague25/badges-alt/43.png"


def send_message_viber(message, image):
    payload = {
        "auth_token": viber_token,
        "from": user_id,
        "type": "picture",
        "text": message,
        "media": image,
        "thumbnail": image,
    }
    r = requests.post(url=viber_url, data=json.dumps(payload))


db = mysql.connector.connect(host="localhost", user="root", port=3306, database="games")

terminal = db.cursor()

query = """
CREATE TABLE IF NOT EXISTS EURO_CUP(
    Id INT PRIMARY KEY AUTO_INCREMENT,
    team_name VARCHAR(255),
    abbr VARCHAR(10),
    stadium_name VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    capacity INT,
    image_url TEXT
);
"""

terminal.execute(query)
db.commit()

next_token = None

try:

    while True:

        if next_token:
            url = Pl_url + "&_next=" + next_token
        else:
            url = Pl_url
        r = requests.get(url=url)
        if r.status_code == 200:
            viber = r.json()
            result = viber["data"]
            for i in result:
                image = f"https://resources.premierleague.com/premierleague25/badges-alt/{i['id']}.png"
                upload = [
                    i["name"],
                    i["abbr"],
                    i["stadium"]["name"],
                    i["stadium"]["city"],
                    i["stadium"]["country"],
                    i["stadium"]["capacity"],
                    image,
                ]
                query = f"Insert into Euro_CUP (team_name,abbr,stadium_name,city,country,capacity,image_url) values(%s,%s,%s,%s,%s,%s,%s)"

                terminal.execute(query, upload)

            db.commit()

            next_token = viber["pagination"]["_next"]
            if next_token is None:
                break

        else:
            print("API Error")
            break

except Exception as e:
    print("Error:", e)

user_choice = input("Enter the team name:").lower()

query = "select * from Euro_CUP where team_name =%s"
terminal.execute(
    query,
    (user_choice,),
)
result = terminal.fetchall()
if result:
    for i in result:
        message = f"""{i[1]} {i[2]} Football Club plays their home matches at the {i[3]} in {i[4]} {i[5]} which has a seating capacity of {i[6]}."""
        image = i[7]
    send_message_viber(message, image)
else:
    print("Invalid Team Name")
