import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "7": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "7": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
            
    return winnings, winning_lines


def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()
            

def deposit():
    while True:
        deposit = input("Enter deposit amount: $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print("Invalid amount (must be greater than 0).")
        else:
            print("Please enter a number.")
    return deposit


def get_number_of_lines():
    while True:
        bets = input(f"Enter your number of lines to bet on (1-{MAX_LINES}): ")
        if bets.isdigit():
            bets = int(bets)
            if 1 <= bets <= MAX_LINES:
                break
            else:
                print("Invalid number.")
        else:
            print("Please enter a number.")
    return bets


def get_bet():
    while True:
        bet = input("Enter bet amount for each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Invalid amount. Must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"Insufficient funds. Your current balance is ${balance}")
        else:
            print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")
            confirm = input("Confirm? (y/n): ")
            if confirm == 'y':
                break
            elif confirm == 'n':
                continue
            else:
                print("Invalid option.")
                continue
    
    
    slots = get_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings > 0:
        print(f"You won ${winnings}.")
        print(f"Lines won on:", *winning_lines)
    else:
        print("You lost.")
        
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == 'q':
            break
        balance += spin(balance)
    print(f"You left with ${balance}")
    
main()
