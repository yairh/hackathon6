class Profile:

    def __init__(self, name, wealth, skills):
        """Create profile """
        self.name = name
        self.wealth = wealth
        self.skills = skills

    def __repr__(self):
        return 'Profile ------\nname: %s\nwealth: %dh\nskills: %s' % (self.name, self.wealth, self.skills)


class Transaction:

    def __init__(self, giver, receiver, amount):
        self.giver = giver
        self.receiver = receiver
        self.amount = amount
        self.status = 'Pending'

    def __repr__(self):
        return 'Transaction Object\nGiver: %s\nReceiver: %s\nAmount: %d' % (self.giver.name, self.receiver.name, self.amount)

    def run(self):
        self.giver.wealth -= self.amount
        self.receiver.wealth += self.amount
        self.status = 'Done'


class Job:

    def __init__(self,id, ,status='Pending'):
        self.id = id
        self.status = status
        self.

    def accept(self,):
        self.

    def make_transaction(self,amount):
        self.transaction = Transaction(,amount)

    def run(self):
        self.transaction.run()



