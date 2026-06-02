import requests
import json

pdf_url = "https://github.com/progit/progit2/releases/download/2.1.449/progit.pdf"

response = requests.get(pdf_url)

with open("progit.pdf", "wb") as file:
    file.write(response.content)

json_url = "http://api.open-notify.org/astros.json"

data = requests.get(json_url).json()

with open("astros.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("файли збережені")