import json
print(2)
with open('champions_data.json', encoding="utf8") as f:
    print(3)
    data = json.load(f)
print(1)

#data = json.load(champions_file)
data = data.get('data')
new_data = []
if not data:
    print('No data found')
    exit()
for champion in data:
    champ_data = {
        'name': None,
        'key' : None,
        'thumb': None,
    }
    champion = data.get(str(champion))
    champ_data['name'] = champion.get('name')
    champ_data['key'] = champion.get('key')
    new_data.append(champ_data)

with open('cleaned_champion_data.json', 'w') as outfile:
    json.dump(new_data, outfile)
    


