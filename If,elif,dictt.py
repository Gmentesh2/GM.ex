
Alien_colour = "Green"
if Alien_colour == "Green":
    print("You have just earned 5 points")
else:
    print("You earned 10 points")

usernames = ["admin","natasha","chusta","giulia","opelia"]
for username in usernames:
    if username == "admin":
        print("Hello admin,would you like to see a report status?")
    else:
        print("Hello "+ username + " for logging in again.")

if Alien_colour == "Green":
    print("\nPlayer earned 5 points")
elif Alien_colour == "Yellow":
    print("Player earned 10 points")
elif Alien_colour == "Red":
    print("Player earned 15 points")
else:
    print("Player earned 0 points")

Alien_colour1 = {"colour": "green","points": 5}
print(Alien_colour1)
print(Alien_colour1["colour"])
print(Alien_colour1["points"])

Alien_colour = Alien_colour1.get("colour")
print(Alien_colour)
Alien_points = Alien_colour1.get("points")
print(Alien_points)
Alien_colour1 = {"colour": "green","points": 5}
print(Alien_colour1)
Alien_colour1["X"] = 0 
Alien_colour1["Y"] = 2
print(Alien_colour1)

alien_colour = {}
alien_colour["colour"] = "black".title()
alien_colour["points"] = 15
print(alien_colour)

Alien_colour1 = {"colour": "green","points": 5}
print(Alien_colour1)
del Alien_colour1["points"]
print(Alien_colour1)

alien_colour = {"colour":"red","points": 10}
print(alien_colour)
del alien_colour["points"]
print(alien_colour)

alien_colour = {"colour":"red","points": 10}
print(alien_colour)
alien_colour["colour"] = "blue"
alien_colour["points"] = 20
print(alien_colour)

fav_languages = {
    "jane": "python",
    "lucas": "C#",
    "mary": "javascipt",
    "show": "C++"
}
print(fav_languages)

for name, languages in fav_languages.items():
  print(name + ': ' + languages)


fav_languages = {
    "jane": "python",
    "lucas": "C#",
    "mary": "javascipt",
    "show": "C++"
}
print(fav_languages)

for language in fav_languages.values():
  print(language)
for name in fav_languages.keys():
  print(name)


fav_languages = {
    "jane": "python",
    "lucas": "C#",
    "mary": "javascipt",
    "show": "C++"
}
num_responces = len(fav_languages)
num_responces

users = []
#
new_user = {
  "first_name": "jovani",
  "last_name": "bocacho",
  "username": "Jbocacho"
}
users.append(new_user)
print(users)
new_user = {
    "first_name": "leonardo",
    "last_name": "davinci",
    "username": "Ldavinci"
}
users.append(new_user)
print(users)

users = []

new_user = {
  "first_name": "jovani",
  "last_name": "bocacho",
  "username": "Jbocacho"
}
users.append(new_user)

new_user = {
    "first_name": "leonardo",
    "last_name": "davinci",
    "username": "Ldavinci"
}
users.append(new_user)

for user_dict in users:
  for k, v in user_dict.items():
    print(k + ": " + v)
  print("\n")

fav_languages = {
    "sara": ["python","C#"],
    "jonas":["java","python"],
    "george":["C++"],
    "lucas":["SQL","C"]
}

for name, LANGS in fav_languages.items():
  print(name + ":")
  for LANG in LANGS:
    print("-" + LANG)
  print("\n")

promt = "Here you can ask the question "
promt += "  and program will answer you immediately."
promt += "Untill you ask \"where is my money?"" , you cant shut down the program"
message = ""
while message != "Where is my money?":
  message = input(promt)
  if message != "Where is my money?":
    print(message)

promt = "Here you can ask the question "
promt += "  and program will answer you immediately."
promt += "Untill you ask \"where is my money?"" , you cant shut down the program."
message = True

while message != "Ask":
  message = input(promt)
  if message != "Ask":
    print(message)



Alien_colour = "Green"
if Alien_colour == "Green":
    print("You have just earned 5 points")
else:
    print("You earned 10 points")

usernames = ["admin","natasha","chusta","giulia","opelia"]
for username in usernames:
    if username == "admin":
        print("Hello admin,would you like to see a report status?")
    else:
        print("Hello "+ username + " for logging in again.")

if Alien_colour == "Green":
    print("\nPlayer earned 5 points")
elif Alien_colour == "Yellow":
    print("Player earned 10 points")
elif Alien_colour == "Red":
    print("Player earned 15 points")
else:
    print("Player earned 0 points")

Alien_colour1 = {"colour": "green","points": 5}
print(Alien_colour1)
print(Alien_colour1["colour"])
print(Alien_colour1["points"])

Alien_colour = Alien_colour1.get("colour")
print(Alien_colour)
Alien_points = Alien_colour1.get("points")
print(Alien_points)
Alien_colour1 = {"colour": "green","points": 5}
print(Alien_colour1)
Alien_colour1["X"] = 0 
Alien_colour1["Y"] = 2
print(Alien_colour1)

alien_colour = {}
alien_colour["colour"] = "black".title()
alien_colour["points"] = 15
print(alien_colour)

Alien_colour1 = {"colour": "green","points": 5}
print(Alien_colour1)
del Alien_colour1["points"]
print(Alien_colour1)

alien_colour = {"colour":"red","points": 10}
print(alien_colour)
del alien_colour["points"]
print(alien_colour)

alien_colour = {"colour":"red","points": 10}
print(alien_colour)
alien_colour["colour"] = "blue"
alien_colour["points"] = 20
print(alien_colour)

fav_languages = {
    "jane": "python",
    "lucas": "C#",
    "mary": "javascipt",
    "show": "C++"
}
print(fav_languages)

for name, languages in fav_languages.items():
  print(name + ': ' + languages)


fav_languages = {
    "jane": "python",
    "lucas": "C#",
    "mary": "javascipt",
    "show": "C++"
}
print(fav_languages)

for language in fav_languages.values():
  print(language)
for name in fav_languages.keys():
  print(name)


fav_languages = {
    "jane": "python",
    "lucas": "C#",
    "mary": "javascipt",
    "show": "C++"
}
num_responces = len(fav_languages)
num_responces

users = []
#
new_user = {
  "first_name": "jovani",
  "last_name": "bocacho",
  "username": "Jbocacho"
}
users.append(new_user)
print(users)
new_user = {
    "first_name": "leonardo",
    "last_name": "davinci",
    "username": "Ldavinci"
}
users.append(new_user)
print(users)

users = []

new_user = {
  "first_name": "jovani",
  "last_name": "bocacho",
  "username": "Jbocacho"
}
users.append(new_user)

new_user = {
    "first_name": "leonardo",
    "last_name": "davinci",
    "username": "Ldavinci"
}
users.append(new_user)

for user_dict in users:
  for k, v in user_dict.items():
    print(k + ": " + v)
  print("\n")

fav_languages = {
    "sara": ["python","C#"],
    "jonas":["java","python"],
    "george":["C++"],
    "lucas":["SQL","C"]
}

for name, LANGS in fav_languages.items():
  print(name + ":")
  for LANG in LANGS:
    print("-" + LANG)
  print("\n")

requesting_toppings =["mushrooms","extra cheese"]

if "mushrooms" in requesting_toppings:
    print("adding mushrooms")
if "peperoni" in requesting_toppings:
    print("adding peperoni")
if "extra cheese" in requesting_toppings:
    print("adding extra cheese")

print("\nfinishing your pizza".title())

if "mushrooms" in requesting_toppings:
    print("\nadding mushrooms")
elif "peperoni" in requesting_toppings:
    print("adding peperoni")
elif "extra cheese" in requesting_toppings:
    print("adding extra cheese")


age_of_person = 2
if age_of_person <= 2:
    print("The person is a baby")
elif age_of_person <=4:
    print("The person is toddler")
elif age_of_person <= 13:
    print("The person is kid")
elif age_of_person <= 20:
    print("The person is teenager")
elif age_of_person <= 65:
    print("The person is adult")
else:
    print("The person is elder")


# baby = 2
# toddler = 2-4
# kid = 4-13
# teenager = 13-20
# adult = 20-65
# elder < 65
age_of_person = 2
if age_of_person <= 2:
    print("The person is a baby")
elif age_of_person <=4:
    print("The person is toddler")
elif age_of_person <= 13:
    print("The person is kid")
elif age_of_person <= 20:
    print("The person is teenager")
elif age_of_person <= 65:
    print("The person is adult")
else:
    print("The person is elder")


requesting_toppings =["mushrooms","extra cheese"]

if "mushrooms" in requesting_toppings:
    print("adding mushrooms")
if "peperoni" in requesting_toppings:
    print("adding peperoni")
if "extra cheese" in requesting_toppings:
    print("adding extra cheese")

print("\nfinishing your pizza".title())

if "mushrooms" in requesting_toppings:
    print("\nadding mushrooms")
elif "peperoni" in requesting_toppings:
    print("adding peperoni")
elif "extra cheese" in requesting_toppings:
    print("adding extra cheese")