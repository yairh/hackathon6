def query_job(job_id, cnx):
    """Query and build Job from database"""
    query = """select t1.id,user_id, t2.status 
            from jobs t1 join statuses t2 
            on t1.status = t2.id where t1.id={};""".format(
        job_id)
    cur = cnx.cursor()
    cur.execute(query)
    job = cur.fetchall()[0]
    cur.close()
    return Job(job_id=job[0], applicant_id=job[1], status=job[2], cnx=cnx)


def query_profile(user_id, cnx):
    """query and build Profile from db"""
    query = """select id, wallet from users where id='{}';""".format(user_id)
    cur = cnx.cursor()
    cur.execute(query)
    profile = cur.fetchall()[0]
    cur.close()
    return Profile(profile[0], profile[1])


class Profile:

    def __init__(self, user_id, wealth):
        """Create profile """
        self.id = user_id
        self.wealth = wealth

    def __repr__(self):
        return 'Profile ------\nId: %s\nwealth: %dh' % (self.id, self.wealth)

    def update_wallet(self, new_value, cnx):
        cur = cnx.cursor()
        query = """update users set wallet= '{}' where id='{}';""".format(new_value, self.id)
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
            self.giver.id, self.receiver.id, self.amount)

    def run(self, cnx):
        self.giver.update_wallet(self.giver.wealth - self.amount, cnx)
        self.receiver.update_wallet(self.receiver.wealth + self.amount, cnx)
        self.status = 'Done'


class Job:

    def __init__(self, job_id, applicant_id, status, cnx):
        self.id = job_id
        self.applicant = query_profile(applicant_id, cnx)
        self.status = status
        self.worker = None
        self.transaction = None

    def __repr__(self):
        return 'Job Object:\nId: %d\napplicant: %s\nworker: %s\nstatus: %s' % (
            self.id, self.applicant, self.worker, self.status)

    def accept(self, worker_id, cnx):
        self.worker = query_profile(worker_id, cnx)
        self.status = 'Pending'
        self.update_status(cnx)

    def make_transaction(self, amount):
        self.transaction = Transaction(self.applicant, self.worker, amount)

    def run(self, cnx):
        self.transaction.run(cnx)
        self.status = 'Complete'
        self.update_status(cnx)

    def update_status(self, cnx):
        """update status to db"""
        query = """update jobs set status=(select id from statuses where status='{}'), worker_id='{}' where id='{}';""".format(
            self.status, self.worker.id, self.id)
        cur = cnx.cursor()
        cur.execute(query)
        cur.close()
