print('---'*100)

fifa_world_cup_2026 = {
    "tournament": "FIFA World Cup 2026",
    "edition": 23,
    "hosts": ["United States", "Canada", "Mexico"],
    "start_date": "2026-06-11",
    "final_date": "2026-07-19",
    "teams": 48,
    "groups": 12,
    "teams_per_group": 4,
    "total_matches": 104,
    "group_stage_matches_per_team": 3,
    "qualification_format": {
        "automatic_qualifiers": "Top 2 teams from each group",
        "additional_qualifiers": "8 best third-placed teams",
        "total_knockout_teams": 32
    }
}
fifa = fifa_world_cup_2026
#print(fifa["total_matches"])
#print(fifa.get("hosts"))
#print(fifa.get("start_date"),fifa.get("final_date"))
#print(fifa.get('qualification_format')['total_knockout_teams'])

#fifa = fifa_world_cup_2026['qualification_format']['automatic_qualifiers']
#print(fifa)
fifa['Trophy_material'] = "Gold"
#print(fifa)
del fifa['edition']
print(fifa)