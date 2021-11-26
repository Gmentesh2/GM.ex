promt = "Here you can ask the question "
promt += "  and program will answer you immediately."
promt += "Untill you ask \"where is my money?"" , you cant shut down the program."
message = True

while message != "Ask":
  message = input(promt)
  if message != "Ask":
    print(message)

promt = "Here you can ask the question "
promt += "  and program will answer you immediately."
promt += "Untill you ask \"where is my money?"" , you cant shut down the program"
message = ""
while message != "Where is my money?":
  message = input(promt)
  if message != "Where is my money?":
    print(message)