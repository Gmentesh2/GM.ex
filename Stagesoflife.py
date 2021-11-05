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
