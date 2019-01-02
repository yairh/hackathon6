import conf
import mysql.connector

from classes import *


def connect_todb(file):
    cnx = mysql.connector.connect(user=file.username, password=file.pw, port=file.prt, database=file.database)
    return cnx


# connect to fb
cnx = connect_todb(conf)

# query available job

user1 = query_profile(1, cnx)
user2 = query_profile(2, cnx)

job = query_job(1, cnx)
print(job)
job.accept(2, cnx)
print(job)
job.make_transaction(10)
print(job.transaction)
job.run(cnx)
print(job)
cnx.commit()
cnx.close()
