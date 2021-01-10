from utils.crud import *
from heading import header

print(header)
CHOICE = """
0. Create table
1. Create account
2. Add amount
3. Spend amount
4. view total amount
5. Delete table
9. Quit
: """
choice = int(input(CHOICE))

while choice != 9:
    if choice in [0, 1, 2, 3, 4, 5]:
        if choice == 0:
            create_table()
        elif choice == 1:
            create_account()
        elif choice == 2:
            wallet_id = int(input("Wallet Id: "))
            amount = int(input("Enter an amount: "))
            add_amount(wallet_id, amount)
            print("Amount added. \n")
        elif choice == 3:
            wallet_id = int(input("Wallet Id: "))
            amount = int(input("Enter an amount: "))
            spend_amount(wallet_id, amount)
            print("Amount deducted. \n")
        elif choice == 4:
            wallet_id = int(input("Enter wallet id: "))
            wallet = view_amounts(wallet_id)
            print(
                "\nWallet Id: {} | Total Amount: {} | Total Amount Added: {} | Total Amount Spent: {}".format(
                    wallet[0], wallet[1], wallet[2], wallet[3]
                )
            )
        elif choice == 5:
            confirm = input(
                "Are you sure, You want to delete the table? (y/n): "
            ).lower()
            if confirm == "y":
                drop_table()
                print("Table deleted.")
            break
        choice = int(input(CHOICE))
    else:
        print("Invalid option.")
        break