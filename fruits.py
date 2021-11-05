fruits = ["bannana","strawberry","apple"]

if "bannana" in fruits:
    print("Do you really like bannana?")
if "apple"in fruits:
    print("Do you really like apple?")
if "orange" in fruits:
    print("Do you really like orange?")

#for loop and if 
requested_toppings = ["mushrooms","green peppers","extra cheese"]

for requested_topping in requested_toppings:
    print("Adding "   +  requested_topping + ".")

print("\nFinished making your pizza")


for requested_topping in requested_toppings:
    if requested_topping == "mushrooms":
        print("Sorry we are out of green peppers right now")
    else:
        print("adding ".title() + requested_topping+".")
print("\nFinished making your pizza")
requested_toppings = ["Pizza"]
if requested_toppings:
    print("Storage is not empty")
else:
    print("Storage is empty")

available_toppings = ["olives","green peppers","pepperoni","pineapple","mushrooms"]
requested_toppings = ["mushrooms","green peppers"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("adding ".title() + requested_topping+".")
    else:
        print("Sorry we dont have requested toppings")
print("\nFinished making your pizza")


