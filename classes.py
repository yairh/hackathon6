import mysql.connector
from conf import username, pw, prt, database


def query_job(job_id):
    """Query and build Job from database"""
    cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
    cur = cnx.cursor()
    query = """select t1.id,user_id,worker_id, t2.status 
            from jobs t1 join statuses t2 
            on t1.status = t2.id where t1.id={};""".format(
        job_id)
    cur.execute(query)
    job = cur.fetchall()[0]
    cnx.commit()
    cnx.close()
    return Job(job_id=job[0], applicant_id=job[1], worker_id=job[2], status=job[3])


def query_profile(user_id):
    """query and build Profile from db"""
    cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
    cur = cnx.cursor()
    query = """select id, wallet from users where id='{}';""".format(user_id)
    cur.execute(query)
    profile = cur.fetchall()[0]
    cnx.commit()
    cnx.close()
    return Profile(profile[0], profile[1])


def update_worker(user_dic):
    cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
    cur = cnx.cursor()

    query = """
        SELECT id
        FROM jobs
        WHERE user_id=(select id from users where username=%s)
        AND skill_id=(select id from skills where skill=%s)
        AND status=(select id from statuses where status='Available')
        LIMIT 1
        """

    cur.execute(query, [user_dic['username'], user_dic['skill']])

    the_id = cur.fetchall()

    query = """
                UPDATE jobs
                set worker_id=(select id from users where username=%s),
                status=(select id from statuses where status='Pending')
                WHERE id=%s"""

    cur.execute(query, [user_dic['worker_name'], the_id[0][0]])
    cnx.commit()
    cnx.close()

    ## this wont work without specifying or selecting the job id


class Profile:

    def __init__(self, user_id, wealth):
        """Create profile """
        self.id = user_id
        self.wealth = wealth

    def __repr__(self):
        return 'Profile ------\nId: %s\nwealth: %dh' % (self.id, self.wealth)

    def update_wallet(self, new_value):
        cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
        cur = cnx.cursor()
        query = """update users set wallet= '{}' where id='{}';""".format(new_value, self.id)
        cur.execute(query)
        cnx.commit()
        cnx.close()


class Transaction:

    def __init__(self, giver, receiver, amount):
        self.giver = giver
        self.receiver = receiver
        self.amount = amount
        self.status = 'Pending'

    def __repr__(self):
        return 'Transaction Object\nGiver: %s\nReceiver: %s\nAmount: %d' % (
            self.giver.id, self.receiver.id, self.amount)

    def run(self):
        self.giver.update_wallet(self.giver.wealth - self.amount)
        self.receiver.update_wallet(self.receiver.wealth + self.amount)
        self.status = 'Done'


class Job:

    def __init__(self, job_id, applicant_id, worker_id, status):
        self.id = job_id
        self.applicant = query_profile(applicant_id)
        self.status = status
        self.worker = query_profile(worker_id)
        self.transaction = None
        self.time = None

    def __repr__(self):
        return 'Job Object:\nId: %d\napplicant: %s\nworker: %s\nstatus: %s' % (
            self.id, self.applicant, self.worker, self.status)

    def start(self):
        self.status = 'Starting'
        self.update_status()

    def progress(self):
        self.status = 'In Progress'
        self.time = 'start_time'
        self.update_status()
        self.update_time()

    def finish(self, amount):
        self.transaction = Transaction(self.applicant, self.worker, amount)
        self.status = 'Finishing'
        self.update_status()

    def complete(self):
        self.transaction.run()
        self.status = 'Complete'
        self.time = 'complete'
        self.update_status()
        self.update_time()

    def update_status(self):
        """update status to db"""
        cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
        cur = cnx.cursor()
        query = """update jobs set status=(select id from statuses where status='{}');""".format(
            self.status)
        cur.execute(query)
        cnx.commit()
        cnx.close()

    def update_time(self):
        cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
        cur = cnx.cursor()
        query = """update jobs set {}=now();""".format(
            self.time)
        cur.execute(query)
        cnx.commit()
        cnx.close()
