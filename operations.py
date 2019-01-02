import mysql
from hackathon6.transaction import *


def connect_todb(file):
    cnx = mysql.connector.connect(host=file.host, user=file.user, password=file.password)
    return cnx


def query_job(id, cnx):
    """Query and build Profile from database"""
    query = """select * from available_jobs where job_id={}""".format(id)
    cur = cnx.cursor()
    cur.execute(query)
    job = cur.fetchall()
    cur.close()
    return Job(job[0], job[1], job[2])


def make_transaction(job_id, amount, cnx):
    giver = query_job(job_id, cnx)
    trans = Transaction(job_id, amount)
    return Transaction


def update_job(job, cnx):
    if job.status == 'Pending':
        raise Exception('Pending Transaction cannot be updated. Please run the transaction before updating')
