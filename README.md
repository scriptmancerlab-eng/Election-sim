## Election Calculator

A Python project to simulate elections with various electoral systems.

### Main Features
- **Set Parliament Size:** Choose the number of seats in the parliament.
- **Custom Party Setup:** Select the number of parties and assign each a unique name.
- **Flexible Percentage Input:** Assign a support percentage to each party; includes a warning if percentages don't sum to 100%.
- **Winner/Loser Calculation:** Automatically determines the party with the highest (winner) and lowest (loser) support.
- **Multiple Electoral Systems:** Choose between First Past The Post (FPTP) and Proportional Representation (PR). Additional systems coming soon.
- **Number of Voters** (recently added): You can assign the number of voters that participated in the election, and the number will be assigned to the corresponding percentage

### Usage
1. Install EXE
2. Follow the prompts to enter:
    - Total number of seats
    - Number of parties
    - Each party's name and support percentage
    - Choice of electoral system
3. View election results, including winner/loser and seat allocation by system.

### Example Output
```
Enter number of voters: 125345
Total seats in parliament: 200
How many parties? 5
Enter party name: Party 1
Support for Party 1 (0-100): 50
Enter party name: Party 2
Support for Party 2 (0-100): 25
Enter party name: Party 3
Support for Party 3 (0-100): 10
Enter party name: Party 4
Support for Party 4 (0-100): 10
Enter party name: Party 5
Support for Party 5 (0-100): 5

Parties involved in the election:
     Party 1: 50.00%  →  62672 voters
     Party 2: 25.00%  →  31336 voters
     Party 3: 10.00%  →  12534 voters
     Party 4: 10.00%  →  12534 voters
     Party 5: 5.00%  →  6267 voters
Sum of percentages = 100.00%

Winner: Party 1 has a majority!

Winner: Party 1 with 50.00%
Loser: Party 5 with 5.00%

Select electoral system:
1. First Past The Post (FPTP)
2. Proportional Representation (PR)
Enter your choice (1 or 2): 2

Seat Allocation:
     Party 1: 100 seats
     Party 2: 50 seats
     Party 3: 20 seats
     Party 4: 20 seats
     Party 5: 10 seats
```

### Planned Improvements
- Support for more electoral systems (e.g., Single Transferable Vote, Mixed-Member Proportional). FPTP is also in the works, as it doesn't have a universal way of doing it, and is individual to each country that has it. 
- GUI interface (when I learn how to do it)
- Data export options (CSV/JSON) (whenever I get to learning this too)

