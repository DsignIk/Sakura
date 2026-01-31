import json

data = {
    "browser": False,
    "blue": 61,
    "red": 204,
    "green": 114
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
