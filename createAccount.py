from account import Account
from investmentAccount import InvestmentAccount


def main():

    acct_name = input("Enter name: ")
    acct_num = input("Enter account number: ")
    print("Which type of account do you want to open?")
    choice = int(input("Enter 1 for savings account and 2 for investment account: "))
    if choice == 1:
        savingsAcct(acct_name, acct_num)
    elif choice == 2:
        investmentAcct(acct_name, acct_num)


def savingsAcct(acct_name, acct_num):
    acct1 = Account(acct_name, acct_num)
    print("Balance: ", acct1.balance)
    oper = 0
    while oper != 3:
        oper = int(input("Enter 1 for deposit, 2 for withdrawal, 3 for exit: "))
        if oper == 1:
            amount = int(input("Enter deposit amount: "))
            acct1.deposit(amount)
            print("Balance: ", acct1.balance)
        elif oper == 2:
            amount = int(input("Enter withdrawal amount: "))
            acct1.withdrawal(amount)
            print("Balance: ", acct1.balance)
    print(acct1)


main()
