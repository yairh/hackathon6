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
    cnx.close()
    return Job(job_id=job[0], applicant_id=job[1], worker_id=job[2], status=job[3])


def query_profile(user_id):
    """query and build Profile from db"""
    cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
    cur = cnx.cursor()
    query = """select id, wallet from users where id={};""".format(user_id)
    cur.execute(query)
    profile = cur.fetchall()[0]
    cnx.close()
    return Profile(profile[0], profile[1])


def update_worker(user_dic):
    """update the worker status, and job status run after job query"""
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


def gift_card(giver_id, receiver_id, amount):
    giver = query_profile(giver_id)
    receiver = query_profile(receiver_id)
    Transaction(giver, receiver, amount).run()


# def loan(giver_id, receiver_id, amount):
#     giver = query_profile(giver_id)
#     receiver = query_profile(receiver_id)


class Profile:

    def __init__(self, user_id, wealth):
        """Create profile """
        self.id = user_id
        self.wealth = wealth

    def __repr__(self):
        return 'Profile ------\nId: %s\nwealth: %dh' % (self.id, self.wealth)

    def update_wallet(self, job_id, operation='+'):
        cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
        cur = cnx.cursor()
        query = """update users 
                set wallet=({} {} (select minute(timediff(complete_time,start_time)) 
                from jobs where id={}))
                where id={};""".format(self.wealth, operation, job_id, self.id)
        cur.execute(query)
        cnx.commit()
        cnx.close()


class Transaction:

    def __init__(self, giver, receiver, job_id):
        self.giver = giver
        self.receiver = receiver
        self.job_id = job_id
        self.status = 'Pending'

    def __repr__(self):
        return 'Transaction Object\nGiver: %s\nReceiver: %s\nJob_id: %d' % (
            self.giver.id, self.receiver.id, self.job_id)

    def run(self):
        self.giver.update_wallet(self.job_id, '-')
        self.receiver.update_wallet(self.job_id, '+')
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

    def finish(self):
        self.status = 'Finishing'
        self.update_status()

    def complete(self):
        self.status = 'Complete'
        self.time = 'complete_time'
        self.update_status()
        self.update_time()
        Transaction(self.applicant, self.worker, self.id).run()

    def update_status(self):
        """update status to db"""
        cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
        cur = cnx.cursor()
        query = """update jobs set status=(select id from statuses where status='{}') where id={};""".format(
            self.status, self.id)
        cur.execute(query)
        cnx.commit()
        cnx.close()

    def update_time(self):
        cnx = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
        cur = cnx.cursor()
        query = """update jobs set {}=now() where id={};""".format(
            self.time, self.id)
        cur.execute(query)
        cnx.commit()
        cnx.close()
