import json
import os

# JSON file setup
data_file = "data.json"

# Load from JSON or set default
if os.path.exists(data_file):
    with open(data_file, "r") as file:
        data = json.load(file)
else:
    data = {
        "actual_card_number": 54321,
        "actual_pin": "Passwd",
        "actual_balance": 3000,
        "withdraw_history": [],
        "deposit_history": []
    }

print("*" * 10)
print("Welcome To Data Bank")
print("*" * 10)

def login():
    """
       Handles user login by asking for card number and PIN.
       Repeats input until both are correct.

       Returns:
           tuple: (card_number, pin_number)
       """
    card_number = int(input("Please enter your card number: "))
    pin_number = input("Please enter your PIN: ")
    while card_number != data["actual_card_number"]:
        print("card number is wrong")
        card_number = int(input("Please enter the correct card number: "))
    while pin_number != data["actual_pin"]:
        print("password is wrong")
        pin_number = input("Please enter your correct password: ")
    return card_number, pin_number

def save_data():
    with open(data_file, "w") as file:
        json.dump(data, file)

def account_operations():
    """
        Displays the main menu and performs account operations:
        - Withdraw
        - Deposit
        - Check Balance
        - View Transaction History
        - Quit

        Updates data and saves changes to JSON after each transaction.
        """
    while True:
        main_message = int(input("Select your option (Withdraw[1] Deposit[2] Balance[3] Transaction[4] Quit[5]): "))

        if main_message not in [1, 2, 3, 4, 5]:
            print("Invalid Input")

        elif main_message == 1:
            withdraw_prompt = int(input("Enter the amount: "))
            if withdraw_prompt <= 0:
                print("Enter a valid amount")
            elif withdraw_prompt > data["actual_balance"]:
                print("Insufficient Balance")
                print("Account Number", "Previous Balance", "Withdraw Amount", "Remain Balance")
                print(data["actual_card_number"], data["actual_balance"], withdraw_prompt, data["actual_balance"])
            else:
                old_balance = data["actual_balance"]
                new_balance = old_balance - withdraw_prompt
                data["actual_balance"] = new_balance
                print("Account Number        Previous Balance        Withdraw Amount       New Balance")
                print("   ", data["actual_card_number"], "                 ", old_balance, "                 ", withdraw_prompt,
                      "               ", new_balance)
                data["withdraw_history"].append(withdraw_prompt)
                save_data()

        elif main_message == 2:
            deposit_prompt = int(input("Enter the amount: "))
            if deposit_prompt <= 0:
                print("Enter a valid amount")
            else:
                old_balance = data["actual_balance"]
                new_balance = old_balance + deposit_prompt
                data["actual_balance"] = new_balance
                print("Account Number        Previous Balance        Deposit Amount        New Balance")
                print("   ", data["actual_card_number"], "                 ", old_balance, "                 ", deposit_prompt,
                      "               ", new_balance)
                data["deposit_history"].append(deposit_prompt)
                save_data()

        elif main_message == 3:
            print("Account Number        Current Balance")
            print("    " + str(data["actual_card_number"]) + "                ", data["actual_balance"])

        elif main_message == 4:
            print("********************")
            print("Transaction  Withdraw")
            for i in range(len(data["withdraw_history"])):
                print(i, "            ", data["withdraw_history"][i])
            print("********************")
            print("Transaction  Deposit")
            for i in range(len(data["deposit_history"])):
                print(i, "            ", data["deposit_history"][i])

        elif main_message == 5:
            print("Good Bye")
            break

def main():
    """
       Entry point of the program.
       Calls login and then opens the account operations menu.
       """
    login()
    account_operations()

if __name__ == "__main__":
    main()
