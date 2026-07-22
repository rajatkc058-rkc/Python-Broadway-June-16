import requests
import csv
url = "https://worldcup26.ir/get/games"
try:
    r = requests.get(url=url)
    if r.status_code == 200:
        data = r.json()
        data2 = data.get("games")
        final_data = data2
        upload = []
        for i in final_data:
            upload_1 = [
                i.get("home_team_id"),
                i.get("away_team_id"),
                i.get("home_team_name_en"),
                i.get("away_team_name_en"),
                i.get("home_score"),
                i.get("away_score"),
                i.get("home_scorers"),
                i.get("away_scorers"),
            ]
            upload.append(upload_1)
        with open("game.csv", "w", newline="", encoding="utf-8") as f:
            game = csv.writer(f)
            game.writerow(
                [
                    "Home_TeamID",
                    "Away_TeamID",
                    "Home_Teamname",
                    "Away_Teamname",
                    "Home_score",
                    "Away_score",
                    "Home_scorer",
                    "Away_scorer",
                ]
            )
            game.writerows(upload)
    else:
        print("something went wrong")
except Exception as e:
    print("Error:", e)
