from accountProtected import Account
from investmentAccountProtected import InvestmentAccount


def main():

    acct_name = input("Enter Name: ")
    acct_num = input("Enter account number: ")
    print("What type of account do you want to open?")
    choice = int(input("Enter 1 for savings, 2 for investment: "))
    if choice == 1:
        savingsAcct(acct_name, acct_num)
    elif choice == 2:
        investmentAcct(acct_name, acct_num)


def savingsAcct(acct_name, acct_num):
    acct1 = Account(acct_name, acct_num)
    print("Balance: ", acct1.getBalance())
    oper = 0
    while oper != 3:
        oper = int(input("Enter 1 for deposit, 2 for withdrawal, 3 for exit: "))
        if oper == 1:
            amount = int(input("Enter deposit amount: "))
            acct1.deposit(amount)
            print("Balance: ", acct1.getBalance())
        elif oper == 2:
            amount = int(input("Enter withdrawal amount: "))
            acct1.withdraw(amount)
            print("Balance: ", acct1.getBalance)
        print(acct1)


def investmentAcct(acct_name, acct_num):
    acct1 = InvestmentAccount(acct_name, acct_num)
    print("Balance: ", acct1.getBalance())
    oper = 0
    while oper != 4:
        oper = int(input("Enter 1 for deposit, 2 for withdrawal, 3 for investment, "
                         "4 to exit: "))
        if oper == 1:
            amount = int(input("Enter deposit amount: "))
            acct1.deposit(amount)
            print("Balance: ", acct1.getBalance())
            print("Available for withdrawal: ", acct1.getBalance() - acct1.getInvestment())
        elif oper == 2:
            amount = int(input("Enter withdrawal amount: "))
            acct1.withdraw(amount)
            print("Balance: ", acct1.getBalance())
            print("Available for withdrawal: ", acct1.getBalance() - acct1.getInvestment())
        elif oper == 3:
            invest = int(input("Enter investment amount: "))
            acct1.setInvestment(invest)
            print("Amount invested: ", acct1.getInvestment())
            print("Amount available for withdrawal: ", acct1.getBalance() - acct1.getInvestment())
    print(acct1)


main()
