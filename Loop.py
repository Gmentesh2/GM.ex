magicians = ["alice","david","karolina"]

print(f"Hello {magicians[0]}")
print(f"Hello {magicians[1]}")
print(f"Hello {magicians[2]}")


for magician in magicians:
    print(f"Hello {magician}")

plumbers = ["Shukri","Siko","Nasta"]

for plumber in plumbers:
    print(f"Waitting on 3 PM {plumber}.")
    print(f"Dont late its my request {plumber.title()}.\n")

print("Looking forward until see you.")    

pizzas = ["Peperoni","Margarita","Karakuli"]

for pizza in pizzas:
    # print(pizza)
    print(f"I like {pizza} pizza.\n")
print("I really love your pizza")

numbers1 = [1,2,3,4,5]
numbers2 =list(range(1,6))
print( numbers1)
print(numbers2)

for number in range(1,6):
    print(number)

even_numbers =list(range(2,11,2))
print(even_numbers)

even_numbers1 = list(range(3,14,1))
print(even_numbers1)

squares = []
for number in list(range(1,12)):
    square = number**2
    squares.append(square)

print(squares)

digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))
print(len(digits))
average = sum( digits) / len(digits)
print(average)
# list comprehension -
squares = [number ** 2 for number in range(1,12)]
print(squares)












