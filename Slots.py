#!bin/python
import random,math
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
MAX_ROWS = 3
MAX_COLS = 3

slot_symbols= {
    "A" : 3,
    "B" : 3,
    "C" : 3,
    "D" : 3
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        new_symbol_list = all_symbols[:]
        for _ in range(rows):
            value = random.choice(new_symbol_list)
            new_symbol_list.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def deposit():
    while True:
        amount = input("How much would you like to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"Thanks for the deposit of ${amount}, enjoy!")
            break  
        else:
            print("Please input Correct amount")
    return amount

def bet_lines():
    while True:
        lines_bet = input("How many lines do you want to bet: ")
        if lines_bet.isdigit():
            lines_bet = int(lines_bet)
            if 0 <= lines_bet <= MAX_LINES: 
                break
            else:
                print("Please enter the correct amount")
    return lines_bet

def bet_money(max_bet, lines_bet):
    while True:
        amount_bet= input(f"How much would you like to bet, you max bet per line is {max_bet}: $")
        if amount_bet.isdigit():
            amount_bet = int(amount_bet)
            if 0 < amount_bet <= max_bet:
                total_bet = max_bet * lines_bet
                break
            else:
                print(f"Enter a correct amount between 1 and {max_bet}")
        else:
            print("Enter a correct amount")    

    return total_bet

def main():
    deposit_amount = deposit()
    lines_bet = bet_lines()
    maximum_bet_allowed = MAX_BET // lines_bet
    slot_symbol = get_slot_machine_spin(MAX_ROWS, MAX_COLS, slot_symbols)
    total_bet = bet_money(maximum_bet_allowed, lines_bet)
    print(f"You are betting: {total_bet}, Good Luck")
main()