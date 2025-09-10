import random
##
#\n and print() = go to next line

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3 
COLS = 3 

#dictonary
#symbols on machine + # of times they appear for user
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #loop through every row
        symbol = columns[0][line] #get symbol and check if its in other rows
        for column in columns: #loop through each column and check for that symbol
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #check if symbol is not the same
                break
        else: #no break means user won
            winnings += values[symbol] * bet #bet = bet on each line
            winning_lines.append(line + 1) #shows what lines won

    return winnings, winning_lines

#what symbols are in each column based on frequency of symbols

#loop through dictionary
#loop through symbol count
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count): #loop through symbols twice in the all_symbols list
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLS): #for every column, generate a certain # of symbols

        #pick random values for each row in the column
        column = []
        current_symbols = all_symbols[:]  #make a copy of all_symbols so that symbols are taken away and not repeated
        for _ in range(ROWS): #loop through # of values needed to generate, which = # of rows in machine
            value = random.choice(current_symbols) #pick random value from list
            current_symbols.remove(value) #remove symbol from current_symbols list
            column.append(value) #add value to column

        columns.append(column) # add column to column list

    return columns

def print_slot_machine(columns):
    for row in range (len(columns[0])): # loop through every row
        for i, column in enumerate (columns): #loop through items inside columns #enumerate gives index and item
            if i != len(columns) - 1:   #if i is not = to max index, print the pipe
                print(column[row], end=" | ") #end tells print statement what to end line with
            else:
                print(column[row], end="") #only print current row

        print()


#deposit asks user for what their betting
#checks that its >0 and a number

def deposit():
    while True:
        amount = input("Enter the amount to deposit: £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("This amount is negative")
        else:
            print("Enter a number")

    return amount

#GNOL checks # of betting lines
#checks its between 1 and max set lines

def get_number_of_lines():
    while True:
        lines = input("Enter number of betting lines (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter valid number of lines")
        else:
            print("Enter a number")

    return lines

#get bet check amount on each line
#amount is between min and max bet

def get_bet():
    while True:
        amount = input("How much are u betting on each line? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} and £{MAX_BET}")
        else:
            print("Enter a number")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You don't have enough money. Current balance is £{balance}")
        else:
            break
    print(
        f"You're betting £{bet} on {lines} lines. Total bet = £{total_bet} ")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won £{winnings} ")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance: £{balance}")
        answer = input("Press enter to play (q to quit): ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with £{balance}")

main()
