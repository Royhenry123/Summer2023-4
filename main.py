MAX_LINES = 3
#Global variables

def deposit():
    """
     Takes user input to determine deposit size.
    :return: amount: the amount of money deposited.
    """
    while True:
        amount = input("Enter deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            # Converts amount from string to int
            if amount > 0:
                break
            else:
                print('Enter digit greater than 0')
        else:
            print('Enter a number')

    return amount


def get_number_lines():
    """
    Gets number of lines to bet on
    :return: lines: The number of lines betted on
    """
    while True:
        lines = input("Enter number of lines to bet (1 to " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            # Converts amount from string to int
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter valid number of lines')
        else:
            print('Enter a number')

    return lines


def main():
    # Testing branching and stuff
    for char in 'Roy':
        print(char)

    balance = deposit()
    lines = get_number_lines()
    print(lines, balance)

main()


