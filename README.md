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
Total seats in parliament: 100
How many parties? 3
Enter party name: Red
Support for Red (0-100): 40
Enter party name: Blue
Support for Blue (0-100): 35
Enter party name: Green
Support for Green (0-100): 25

Parties involved in the election:
         Red: 40.00%
        Blue: 35.00%
       Green: 25.00%
Sum of percentages = 100.00%

Winner: Red with 40.00%
Loser: Green with 25.00%

Select electoral system:
1. First Past The Post (FPTP)
2. Proportional Representation (PR)
Enter your choice (1 or 2): 2

Seat Allocation:
         Red: 40 seats
        Blue: 35 seats
       Green: 25 seats
```

### Planned Improvements
- Support for more electoral systems (e.g., Single Transferable Vote, Mixed-Member Proportional). FPTP is also in the works, as it doesn't have a universal way of doing it, and is individual to each country that has it. 
- GUI interface (when I learn how to do it)
- Data export options (CSV/JSON) (whenever I get to learning this too)

