import json
with open("test.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
a = input('Что вы хотите изменить: ')
records[a] = input('Введите новые данные: ')
with open("test.json", "w") as write_file:
    json.dump(records, write_file)

