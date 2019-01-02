class Profile:

    def __init__(self, user_id, username, wealth):
        """Create profile """
        self.id = user_id
        self.wealth = wealth
        self.name = username

    def __repr__(self):
        return 'Profile ------\nId: %s\nname: %s\nwealth: %dh' % (self.id, self.name, self.wealth)

    def update_wallet(self, new_value, cnx):
        cur = cnx.cursor()
        query = """update users (wallet) values ('{}');""".format(new_value)
        cur.execute(query)
        cur.close()


class Transaction:

    def __init__(self, giver, receiver, amount):
        self.giver = giver
        self.receiver = receiver
        self.amount = amount
        self.status = 'Pending'

    def __repr__(self):
        return 'Transaction Object\nGiver: %s\nReceiver: %s\nAmount: %d' % (
            self.giver.name, self.receiver.name, self.amount)

    def run(self):
        self.giver.update_wallet(self.giver.wealth - self.amount)
        self.receiver.update_wallet(self.receiver.wealth + self.amount)
        self.status = 'Done'


class Job:

    def __init__(self, job_id, user_id, skill, status='Available'):
        self.id = job_id
        self.applicant_id = user_id
        self.status = status
        self.skill = skill
        self.worker_id = None
        self.transaction = None

    def __repr__(self):
        return 'Job Object:\n'

    def accept(self, worker_id, cnx):
        self.worker_id = worker_id
        self.status = 'Pending'
        self.update_status(cnx)

    def make_transaction(self, amount):
        self.transaction = Transaction(self.applicant_id, self.worker_id, amount)

    def run(self, cnx):
        self.transaction.run()
        self.status = 'Done'
        self.update_status(cnx)

    def update_status(self, cnx):
        """update status to db"""
        query = """update available_jobs (status) values (select id from job_status where status='{}');""".format(
            self.status)
        cur = cnx.cursor()
        cur.execute(query)
        cur.close()
