from accountProtected import Account

class InvestmentAccount(Account):

    """constructor"""

    def __init__(self, name, acct_num):
        base = super().__init__(name, acct_num)
        self.__investment = 0

    def getInvestment(self):
        return self.__investment

    def setInvestment(self, invest):
        if invest < 0:
            print("Investment amount cannot be negative.")
        elif invest > self._balance:
            print("Investment amount cannot be more than account balance.")
        else:
            self.__investment = invest

    #  this method overrides the withdraw method in the Account class
    def withdraw(self, amt):
        if amt > self._balance - self.__investment:
            print("Withdrawal denied. Amount exceeds available funds.")
        else:
            self._balance = self._balance - amt

    #  this __str__ method overrides the one in the Account class
    def __str__(self):
        return "Account name: " + self._name + "\nAccount number: " + self._acct_num +\
               "\nInvestment amount: " + str(self.__investment)
