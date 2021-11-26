promt = "Here you can ask the question "
promt += "  and program will answer you immediately."
promt += "Untill you ask \"where is my money?"" , you cant shut down the program."
message = True

while message:
  message = input(promt)
  
  if message == "Ask":
    message = False
  else:
    print(message)

promt = "Here you can ask the question "
promt += "  and program will answer you immediately."
promt += "Untill you ask \"where is my money?"" , you cant shut down the program"
message = ""
while message != "Where is my money?":
  message = input(promt)
  if message != "Where is my money?":
    print(message)

n = 2
while n < 30:
    print(n)
    n += 2 
print(n)


promt = "What citys have you visited"
promt += "\nEnter 'Quit' when you are done.>>>" 

while True:
  city = input(promt)

  if city == "Quit":
    break
  else:
    print("I have been to " + city + ".")

promt = "What citys have you visited"
promt += "\nEnter 'Quit' when you are done.>>>" 

while True:
  city = input(promt)

  if city == "Quit":
    break
  else:
    print("I have been to " + city + ".")
#
Banned_users = ["mak","zac","stark"]

promt = "Add player in your team"
promt += "\nEnter 'quit' when you are done"

players = []

while True:
  player = input(promt)
  if player == "quit":
    break
  elif player in Banned_users:
    print(player + "is banned")
    continue
  else:
    players.append(player)
    print(player)

print("\nYour team list:")
for player in players:
  print(player)