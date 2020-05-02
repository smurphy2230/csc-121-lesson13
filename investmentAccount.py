from account import Account


class InvestmentAccount(Account):

    """constructor"""

    def __init__(self, name, acct_num):

        #  the following two lines are usually combined - super().__init__(name, acct_num)
        base = super()  # this calls the super function which returns a proxy object
        base.__init__(name, acct_num)  # proxy object is used to call init method of base class
        self.__investment = 0  # define private instance variable

    def getInvestment(self):
        return self.__investment

    def setInvestment(self, invest):
        if invest < 0:
            print("Investment amount cannot be negative.")
        elif invest > self.balance:
            print("Investment amount cannot be greater than account balance.")
        else:
            self.__investment = invest


