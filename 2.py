Import json
data = {
    'Фамилия': 'Плтоников',
    'Имя': 'Дмитрий',
    'Отчество': 'Романович',
    'Телефон': '89991234567',
    'Год рождения': 2006,
    'Город рождения': 'Благовещенск',
    'Место учёбы': 'БГПУ'
    }
with open("test.json", "w") as write_file:
    json.dump(data, write_file)
