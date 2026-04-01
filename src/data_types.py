import random
import datetime

cities  = ["Bucuresti", "Iasi", "Fagaras", "Timisoara"]
print(cities[0])        # first item
print(cities[-1])       # last item
print(len(cities))      # count items

person = {
    "name": "Rares",
    "city": "Bucharest",
    "age": 51
}
print(person["name"])
print(person["age"] + 1)

people = [
    {"name": "Rares", "city": "Bucuresti"},
    {"name": "Ana", "city": "Cluj-Napoca"},
    {"name": "Monica", "city": "Brasov"},
]

## print(people[0]["name"] + people[0]["city"])
print(f"This is the line for {people[0]['name']} from {people[0]["city"]}")


## if-then-else
age = 51
if age > 50:
    print("Senior developer")
elif age > 30:
    print("Mid level")
else:
    print("Junior")

## loops

for person in people:
    print(f"{person['name']} lives in {person['city']}")

## functions
print("\n\n## functions\n")

def greet(name, city):
    return f"{name} lives in {city}"

for person in people:
    message = greet(person["name"], person["city"])
    print(message)

## Importing libraries

print("\n\n## Importing libraries\n")

# pick a random person from the list
chosen = random.choice(people)
print(chosen['name'])

today = datetime.date.today()
print(f"Today is {today}")