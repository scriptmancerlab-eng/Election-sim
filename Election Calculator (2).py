def first_past_the_post(parties, percents, total_seats):
    winner_name, winner_percent = get_winner(parties, percents)
    return {winner_name: total_seats}

def proportional_representation(parties, percents, total_seats):
    seats = {}
    remaining_seats = total_seats
    unallocated = 0
    
    for party, percent in zip(parties, percents):
        seat_count = int((total_seats * percent) / 100)
        seats[party] = seat_count
        remaining_seats -= seat_count
        unallocated += (total_seats * percent / 100) - seat_count
    
    while remaining_seats > 0:
        max_remainder = 0
        max_party = None
        for party, percent in zip(parties, percents):
            remainder = (total_seats * percent / 100) - seats[party]
            if remainder > max_remainder:
                max_remainder = remainder
                max_party = party
        if max_party:
            seats[max_party] += 1
            remaining_seats -= 1
    
    return seats

def calculate_seats(parties, percents, total_seats, system="FPTP"):
    if system == "FPTP":
        return first_past_the_post(parties, percents, total_seats)
    elif system == "PR":
        return proportional_representation(parties, percents, total_seats)

def get_total_seats():
    while True:
        try:
            total_seats = int(input("Total seats in parliament: "))
            if total_seats <= 0:
                print("Please enter a positive whole number")
                continue
            return total_seats
        except ValueError:
            print("Please enter a whole number (e.g, 100)")

def get_party_data(num_parties):
    parties = []
    percents = []
    
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
    
    return parties, percents

def display_results(parties, percents):
    print("\nParties involved in the election:")
    for nm, pc in zip(parties, percents):
        print(f"{nm:>12}: {pc:.2f}%")
    
    total_pct = sum(percents)
    print(f"Sum of percentages = {total_pct:.2f}%")
    
    if total_pct != 100:
        print("Warning: percentages do not add up to 100")

def get_winner(parties, percents):
    max_percent = max(percents)
    winner_index = percents.index(max_percent)
    return parties[winner_index], max_percent

def get_loser(parties, percents):
    min_percent = min(percents)
    loser_index = percents.index(min_percent)
    return parties[loser_index], min_percent

def get_num_parties():
    while True:
        try:
            num = int(input("How many parties? "))
            if num <= 0:
                print("Please enter a positive number of parties")
                continue
            return num
        except ValueError:
            print("Please enter a whole number")

def main():
    total_seats = get_total_seats()
    num_parties = get_num_parties()
    parties, percents = get_party_data(num_parties)
    display_results(parties, percents)
    
    winner_name, winner_percent = get_winner(parties, percents)
    if winner_percent >= 50:
        print(f"\nWinner: {winner_name} has a majority!")
    
    loser_name, loser_percent = get_loser(parties, percents)
    print(f"\nWinner: {winner_name} with {winner_percent:.2f}%")
    print(f"Loser: {loser_name} with {loser_percent:.2f}%")
    
    print("\nSelect electoral system:")
    print("1. First Past The Post (FPTP)")
    print("2. Proportional Representation (PR)")
    choice = input("Enter your choice (1 or 2): ")
    
    system = "FPTP" if choice == "1" else "PR"
    seat_allocation = calculate_seats(parties, percents, total_seats, system)
    
    print("\nSeat Allocation:")
    for party, seats in seat_allocation.items():
        print(f"{party:>12}: {seats} seats")

if __name__ == "__main__":
    main()