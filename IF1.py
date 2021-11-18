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


age = 16
if age >= 18:
    print("You are old enough to vote")
    print("Have you registered vote?")
else:
    print("You are too young to participate in the elections")
    print("Wait till become older")


age = 18 
if age < 5:
    print("Your admission cost is free")
elif age <=18:
    print("Your admission cost is another 5$.")
else:
    print("Your admission cost is 15$.")