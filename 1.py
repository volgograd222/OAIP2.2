import json
with open("test.json", "w") as write_file:
    json.dump(data, write_file)
with open("test.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
age_moscow = 0
moscow_person = 0
name = []
for i in range(1, len(records)+1):
    a = f'data{i}'
    b = records[a]
    if b['city'] == 'Moscow':
        age_moscow += b['age']
        moscow_person += 1
        name.append(b['name'])
    else: continue
age_moscow /= moscow_person
print(*name, age_moscow)
