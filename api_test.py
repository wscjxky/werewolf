import requests
roles={
        "hunter": 1,
        "idiot": 1,
        "seer": 1,
        "villager": 4,
        "werewolf": 4,
        "witch": 1,
        # "count":12,
      }
import json
res=requests.post("http://localhost:5000/start_game",json=roles)
print(res.text)

res=requests.post("http://localhost:5000/role",json={"number":4})

print(res.text)
res=requests.post("http://localhost:5000/action",json={"number":4,"role":"werewolf","action":2})
exit()

print(res.text)
res=requests.post("http://localhost:5000/result",json={})

res=requests.post("http://localhost:5000/action",json={"number":5,"role":"witch","action":"save"})

print(res.text)
# res=requests.post("http://localhost:5000/action",json={"number":5,"role":"witch","action":6})
# print(res.text)
res=requests.post("http://localhost:5000/action",json={"number":6,"role":"seer","action":5})

print(res.text)
