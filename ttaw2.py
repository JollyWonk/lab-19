import shelve

countries_area = {
    'Алжир': 2381741,
    'ДР Конго': 2344858,
    'Судан': 1861484,
    'Лівія': 1759540,
    'Чад': 1284000,
    'Нігер': 1267000,
    'Ангола': 1246700,
    'Малі': 1240192,
    'Ефіопія': 1104300,
    'ПАР': 1219090,
}

top_countries = dict(sorted(countries_area.items(), key=lambda x: x[1], reverse=True)[:3])

with shelve.open('africa.dat') as db:
    for country, area in top_countries.items():
        db[country] = area

print("Дані записано у файл africa.dat")

with shelve.open('africa.dat') as db:
    print("Зчитані дані з файлу africa.dat:")
    for country in db:
        print(f"{country}: {db[country]} км²")
