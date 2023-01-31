import json
arquivojson="person.json"
with open(arquivojson,'r') as file:
    parsed=json.load(file)
print(parsed)