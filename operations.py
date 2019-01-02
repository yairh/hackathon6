import mysql.connector
from hackathon6.transaction import *


def connect_todb(file):
    cnx = mysql.connector.connect(user=file.username, password=file.pw, port=file.prt, database=file.database)
    return cnx


def query_job(job_id, cnx):
    """Query and build Profile from database"""
    query = """select * from available_jobs where job_id={};""".format(job_id)
    cur = cnx.cursor()
    cur.execute(query)
    job = cur.fetchall()
    cur.close()
    return Job(job_id=job[0], user_id=job[1], skill=job[2], status=job[3])


def query_profile(user_id, cnx):
    query = """select * from users where id='{}';""".format(user_id)
    cur = cnx.cursor()
    cur.execute(query)
    profile = cur.fetchall()[0]
    cur.close()
    return Profile(profile[0], profile[1], profile[2])


