players = ["Messi","Pogba","Van persie","Rooney"]

print(players[0])
print(players[1:5])
print(players[-2])

co_players = players

print(co_players)

players[-1] = "Messi"
print(players)

print(f"The first three players:{players[0:3]}.")

print("The first three players\n")
print("-" * 12)
for player in players[0:3]:
    print(player)

