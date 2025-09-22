#asks for number of seats
while True:
    try:
        total_seats = int(input("Total seats in parliament: "))
        if total_seats <= 0:
            print("Please enter a positive whole number")
            continue
        break
    except:
        print("Please enter a whole number (e.g, 100)")

parties = []
percents = []

#asks how many parties
num_parties = int(input("How many parties? "))

#asks for % of the parties
for i in range(num_parties):
    name = input("Enter party name: ").strip()
    if name == "":
        name = "Party_" + str(i+1)
            
    while True:
        raw = input(f"Support for {name} (0-100): ") 
        try:
            p = float(raw)
        except:
            print("Please enter a number, e.g, 35.5")
            continue
        if p < 0 or p > 100:
            print("Enter a value between 0 and 100.")
            continue
        break   

    parties.append(name)     
    percents.append(p)       
#assigns and calculates support for each party
print("\nYou entered:")
for nm, pc in zip(parties, percents):
    print(f"{nm:>12}: {pc:.2f}%")
#calculates sum of percentages and warning if its not 100%
print(f"Sum of percentages = {sum(percents): .2f}%")

winner_index = None
winner_percent = None
total_pct = sum(percents)
if total_pct != 100:
    print("Warning: percentages do not add up to 100")
for i in range(len(percents)):
    if winner_percent is None or percents[i] > winner_percent:
        winner_percent = percents[i]
        winner_index = i

if winner_percent >= 50:
    print(f"\nWinner: {parties[winner_index]} has a majority!")
#finds the smallest party
loser_index = None
loser_percent = None

for i in range(len(percents)):
    if loser_percent is None or percents[i] < loser_percent:
        loser_percent = percents[i]
        loser_index = i
#prints winners and losers
print(f"\nWinner: {parties[winner_index]} with {winner_percent:.2f}%")
print(f"Loser: {parties[loser_index]} with {loser_percent:.2f}%")
        