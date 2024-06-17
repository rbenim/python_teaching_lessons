people = [{"name": "Kofi", "address": "Tema" },
          {"name": "Emma", "address": "Accra" },
          {"name": "Yaa", "address": "East Legon" }]


def f(person):
    return person["name"]

people.sort(key=f)

print(people)
