import requests
import pyodbc

db = pyodbc.connect(
    'DRIVER= {SQL Server};SERVER=localhost\SQLEXPRESS02;database=worldcup;Trusted_connection=yes;',autocommit=True
)

terminal = db.cursor()
# query = 'create database worldcup'
# terminal.execute(query)
query = """create table FIFA_GAMES (Homeid int,
Awayid int,
Hometeamname varchar(max),
Awayteamname varchar(max),
Homescore int,
Awayscore int,
Homescorer varchar(max),
Awayscorer varchar(max)
);"""
terminal.execute(query)
db.commit()
url = "https://worldcup26.ir/get/games"
try:
    r = requests.get(url=url)
    if r.status_code == 200:
        data = r.json()
        data2 = data.get("games")
        final_data = data2
        upload = []
        for i in final_data:
            query = "INSERT INTO FIFA_GAMES (Homeid, Awayid, Hometeamname,Awayteamname,Homescore,Awayscore,Homescorer,Awayscorer) Values (?,?,?,?,?,?,?,?)"
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
        terminal.executemany(query,upload)
        db.commit()
    else:
        print("something went wrong")
except Exception as e:
    print("Error:", e)
