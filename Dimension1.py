dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
# # () is mutable , cant modify or else tuffle 
# # [] list is imutable , can modify   

dimensions2 = [200,50]
print(dimensions2[0])
print(dimensions2[1])

dimensions2[0] = 250 
print(dimensions2[0])
print("original dimensions".title())
for dimension in dimensions:
    print(dimension **3)
    print(dimension ** 2)
print("\nModified dimensions")
dimensions = (300,100)
for dimension in dimensions:
    print(dimension **3)
    print(dimension **2)

foods = ("pizza","mtsvadi","khinkali")
foods[3] = "katleti" 
for food in foods:
    print(food)
foods = ("pizza","mtsvadi","khinkali","lobiani")
for food in foods:
    print(food.title())

print("How is your day going?")