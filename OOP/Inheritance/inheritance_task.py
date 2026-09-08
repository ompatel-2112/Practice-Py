import random


class BankInfo:
    def __init__(self,first_name,last_name,gender,address):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address


class BankAccount:
    def __init__(self,amount,bank_info):
        self.acc_no = random.randint(00000000,99999999)
        self.amount = amount
        self.object_BankInfo = bank_info

class Saving(BankAccount):
    minAmount = 10000
    rate = 6

    def valid_amount(self):
        chances = 3
        while chances > 0:
            amt = float(input("Enter initial deposit for Saving Account: "))
            if self.minAmount <= amt :
                self.amount = amt
                return true
            else:
                chances -= 1
                print(" Amount too low! " + str(chances) +" chances left.")

    def calculate_interest(self, months):
        interest = (self.amount * Saving.rate * months) / (12 * 100)
        return interest

class Current(BankAccount, Saving):
    minAmount = 5000
    rate = None
    amount=Saving.valid_amount


class Main:

    def get_bank_info(self):
        fn = input("First Name: ")
        ln = input("Last Name: ")
        gender = input("Gender: ")
        address = input("Address: ")
        return BankInfo(fn, ln, gender, address)

    def run(self):
        bank_info = self.get_bank_info()

        print("\nSelect Account Type:")
        print("1. Saving")
        print("2. Current")
        choice = input("Enter choice (1/2): ")

        if choice == "1":
            amount = self.valid_amount(Saving.minAmount)
            self.account = Saving(amount, bank_info)

        elif choice == "2":
            amount = self.valid_amount(Current.minAmount)
            self.account = Current(amount, bank_info)

        else:
            print("Invalid account type selected.")
            return

        months = int(input("\nEnter number of months: "))
        print("Invalid input for months.")
        interest = self.account.calculate_interest(months)
        print("Months:",months)
        print("Interest:",interest)
        print("Total Balance :", self.account.amount + interest)

r=Main()
r.get_bank_info()
r.run

