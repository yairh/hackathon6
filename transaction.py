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


# p1 = Profile('John', 1, 'Hacking')
# p2 = Profile('James', 10, 'Magic')
# print(p1)
# print(p2)
#
# trans = Transaction(p2,p1,1)
# print(trans)
# print(trans.status)
# trans.run()
# print(trans.status)
# print(p1)
# print(p2)
