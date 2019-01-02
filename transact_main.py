import conf
import mysql.connector

from classes import *


# query available job

user1 = query_profile(1, cnx)
user2 = query_profile(2, cnx)

job = query_job(1)
print(job)
print(job)
print(job.transaction)
job.run(cnx)
print(job)

