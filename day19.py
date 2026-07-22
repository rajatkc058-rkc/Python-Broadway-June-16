# url = "https://markets.onlinekhabar.com/smtm/home/top-companies"
# import requests

# url = "https://markets.onlinekhabar.com/smtm/home/top-companies"

# r = requests.get(url=url)
# if r.status_code == 200:
#     data = r.json()
#     data = data["response"]
#     final_data = data[:10]
#     for i in final_data:
#         print(f"{i['ticker']} {i['ltp']}")

# else:
#     print("something went wrong")

url = "https://markets.onlinekhabar.com/smtm/home/fear-and-greed"

import requests
r = requests .get (url = url)
if r.status_code == 200:
    data = r.json()
    # print(type(data))
    # print(data.keys())
    data2 = data["response"]
    # print(type(data2))
    # print(data)
    final_data = data2
    for i in final_data:
        print(f"{i["value"]} {i["message"]}")
else:
    print("something went wrong")



    