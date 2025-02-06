import requests

response = requests.get("https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")
print(response)

json_of_response = response.json()
items = json_of_response["items"]
for index,question in enumerate(items):
    print(f"{index+1}) {question['title']}")