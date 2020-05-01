from accountPrivate import Account

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
        elif invest > self.getBalance():
            print("Investment amount cannot be greater than account balance.")
        else:
            self.__investment = invest
