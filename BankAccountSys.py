from datetime import datetime

class BankAccount:
    
    bank_name = "Python Bank"  # class variable
    
    def __init__(self,acc_holder,acc_number,balance):
        self.acc_holder =acc_holder
        self.acc_number = acc_number
        self.balance = balance
        self.history = []

    def deposit(self,amount):
        self.balance += amount
        self.history.append(f"Diposited : ₹{amount}")
        print(f"✅ Amount ₹{amount} deposited successfully!")
        print(f"Your Current Balance is : ₹{self.balance}")  


    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawal : ₹{amount}")
            print(f"✅ Amount ₹{amount} withdraw successfully !")
            print(f"Your Current balance is : ₹{self.balance}")
            if self.balance<1000:
                print("❌Low Balance")
        else :
            print("❌ Insufficient Balance !")
            print(f"Your Current balance is : ₹{self.balance}")
        
        
    def display_balance(self):
        print(f"💰 Current Balance : ₹{self.balance} ")

    def display_account_info(self): #To display account holder details:
        print(f"👤 Account Holder: {self.acc_holder}")
        print(f"🏦 Account Number: {self.acc_number}")

    def show_history(self):
        print("📜 Transaction History:")
        for h in self.history:
            print("-", h)

    @staticmethod
    def bank_info():
        print("🏦 Welcome to", BankAccount.bank_name)


# Dictionary to store multiple accounts
accounts = {}

while True:
    print("\n--- Main Menu ---")
    print("1. Create Account")
    print("2. Login to Account")
    print("3. Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            name = input("Enter your name: ")
            acc_no = int(input("Enter your account number: "))
            balance = int(input("Enter initial balance: "))
            pin = int(input("Set your 4-digit PIN: "))
            if acc_no in accounts:
                print("⚠️ Account already exists!")
            else:
                new_acc = BankAccount(name, acc_no, balance)
                accounts[acc_no] = {"object": new_acc, "pin": pin}
                print("✅ Account created successfully!")
        case 2:
            acc_no = int(input("Enter your account number: "))
            if acc_no in accounts:
                for attempt in range(3):
                    entered_pin = int(input("Enter your PIN: "))
                    if entered_pin == accounts[acc_no]["pin"]:
                        print(f"\n✅ Login successful! Welcome {accounts[acc_no]['object'].acc_holder}")
                        user = accounts[acc_no]["object"]   
                        while True:
                            print()
                            print("-----Bank Menu-----")
                            print("1.Deposit")
                            print("2.Withdraw")
                            print("3.Check Balance")
                            print("4.Account Information")
                            print("5.Bank Information")
                            print("6.Account History")
                            print("7.Logout")
                            print()
                            choice = int(input("Enter your choice : "))
                            match choice:
                                case 1:
                                    amount = int(input("Enter amount you want to deposit:"))
                                    user.deposit(amount)
                                case 2:
                                     amount = int(input("Enter amount you want to withdraw:"))
                                     user.withdraw(amount)
                                     
                                case 3:
                                     user.display_balance()

                                case 4:
                                     user.display_account_info() #To display account holder details:

                                case 5:
                                     user.bank_info()
                                     
                                case 6:
                                     user.show_history()
                                     
                                case 7:
                                     print("🚪 Logged out successfully!")
                                     break
                                case _:
                                     print("⚠️ Invalid choice. Please select again.")
                
                        break
                else:
                    print("❌ Account locked after 3 wrong attempts.")

            else:
                print("⚠️ Account not found! Please create an account first.")
        case 3:
            print("👋 Exiting... Thank you for using Python Bank!")
            break

        case _:
            print("❌ Invalid option. Try again.")
                
        
        

            

                
        
