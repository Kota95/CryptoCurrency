class MemPool:

    def __init__(self):
        self.Transactions = []

    def NewTransactions(self, Transaction):
        self.Transactions.append(Transaction)

    def VerifyTransactions(self, Data):
        for i in Data:
            if not i in self.Transactions:
                return False

        return True

    def RemoveTransactions(self, Data):
        try:
            for i in Data:
                self.Transactions.remove(i)

            return True

        except:
            return False

    def GetTransactions(self):
        
        Transactions = """{}""".format("\n".join(self.Transactions))
        return Transactions
