import requests
import json
import time
import mysql.connector

viber_token = '56dbfd241d322b4f-47b755db63e2c85f-6d281e62d622c54a'
user_id = "nffEXekaqSrbdtm2n2kkrQ=="
viber_url = "https://chatapi.viber.com/pa/post"

Pl_url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/2026/teams?pageSize=100"

image_url = "https://resources.premierleague.com/premierleague25/badges-alt/43.png"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    database="games"
)

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

# # Pagination starts from the first page
next_token = None

try:
    
     while True:

        # First request uses the original URL
        # After that, use the next page token
        if next_token:
            url = Pl_url + "&_next=" + next_token
        else:
            url = Pl_url
        # print(url)
        r = requests.get(url=url)

        if r.status_code == 200:

            viber = r.json()
            # print(viber['pagination'])
            result = viber["data"]
            # print(result[0]["name"])

            for i in result:
                image = f"https://resources.premierleague.com/premierleague25/badges-alt/{i['id']}.png"
                upload = [
                i["name"],
                i["abbr"],
                i["stadium"]["name"],
                i["stadium"]["city"],
                i["stadium"]["country"],
                i["stadium"]["capacity"],
                image
                ]
                query = f"Insert into Euro_CUP (team_name,abbr,stadium_name,city,country,capacity,image_url) values(%s,%s,%s,%s,%s,%s,%s)"

                terminal.execute(query,upload )

            db.commit()

            # Read the next page token
            next_token = viber["pagination"]["_next"]

            # If there is no next page, stop looping
            if next_token is None:
                break

        else:
            print("API Error")
            break

except Exception as e:
    print("Error:", e)

# page = 1

# while True:

#     if next_token:
#         url = Pl_url + "&_next=" + next_token
#     else:
#         url = Pl_url

#     r = requests.get(url)
#     data = r.json()

#     print(f"Page: {page}")
#     print("Next Token:", data["pagination"]["_next"])
#     print("-" * 50)

#     next_token = data["pagination"]["_next"]

#     if next_token is None:
#         print("No more pages.")
#         break

#     page += 1