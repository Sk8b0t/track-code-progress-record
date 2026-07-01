import requests
r = requests.get("https://api.agify.io/?name=meelad")
print(r.text)
print(r.status_code)
url = "https://api.agify.io/?name=meelad"
data = {i: f"item-{i}" for i in range(10)}
r2=requests.post(url=url,data=data)
print(r2.text)
print(r2.status_code)
