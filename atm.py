import sys
balance = 10000
while True:
    print("Welcome ot the Automated Teller Machine! To transact, type:")
    print("1 - Check Balance")
    print("2 - Withdraw")
    print("3 - exit")
    transaction = input("Transaction number : ")
    if transaction in ["1", "2", "3"]:
        if transaction == "1":
            print(f"Your current balance is P{balance}.")
        if transaction == "2":
            while True:
                withdraw = int(input("Type in the amount you want to withdraw: "))
                if withdraw > balance:
                    print("The amount is greater than your current balance. Try again.")
                else:
                    balance -= withdraw
                    #define bills denomination here
                    bills = {
                        'thousand': 0,
                        'one_hundred': 0,
                        'twenty': 0,
                        'coins': 0
                    }
                    while True:
                        if withdraw >= 1000:
                            withdraw -= 1000
                            bills.update({'thousand': bills['thousand'] + 1})
                        elif withdraw >= 100:
                            withdraw -= 100
                            bills.update({'one_hundred': bills['one_hundred'] + 1})
                        elif withdraw >= 20:
                            withdraw -= 20
                            bills.update({'twenty': bills['twenty'] + 1})
                        elif withdraw >= 1:
                            withdraw -= 1
                            bills.update({'coins': bills['coins'] + 1})
                        else:
                            break
                    print(f"You have withdrawn P{withdraw}. Here is the denomination of bills:")
                    if bills['thousand'] > 0:
                        print(f"P1000: {bills['thousand']}")
                    if bills['one_hundred'] > 0:
                        print(f"P100: {bills['one_hundred']}")
                    if bills['twenty'] > 0:
                        print(f"P20: {bills['twenty']}")
                    if bills['coins'] > 0:
                        print(f"Coins: {bills['coins']}")
                    break
        if transaction == "3":
                sys.exit("Thank you for using our ATM!")
    else:
        print("Incorrect Input. Please try again.")