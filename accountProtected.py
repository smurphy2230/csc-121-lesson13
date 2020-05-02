class Account:

    """constructor"""

    def __init__(self, name, acct_num):
        self._name = name
        self._acct_num = acct_num
        self._balance = 0

    def deposit(self, amt):
        self._balance = self._balance + amt

    def withdraw(self, amt):
        if amt > self._balance:
            print("Withdrawal denied due to insufficient funds.")
        else:
            self._balance = self._balance - amt

    def getBalance(self):
        return self._balance

    def __str__(self):
        return "Account name: " + self._name + "\nAccount number " + self._acct_num
        + "\nBalance: " + str(self._balance)
