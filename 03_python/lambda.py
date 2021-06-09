people = [
    {"name": "Harry", "house": "Cryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# sorting by creating a function
# def f(person):
#     return person["name"]
#people.sort(key=f)

# sorting by using a lambda
people.sort(key=lambda person: person["house"])

print(people)