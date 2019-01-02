import sys
import logging

import database_queries

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create a file handler
file_handler = logging.FileHandler('hackathon.log')
file_handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(logging.StreamHandler(sys.stdout))  # For printing to stdout

###################

database_queries.create_databases()

import dummy_data

for i in dummy_data.dummy_user_details():
    database_queries.insert_user_details(i)

for i in dummy_data.dummy_skill_categories():
    database_queries.populate_skill_categories(i)

for i in dummy_data.dummy_skills():
    database_queries.populate_skills(i)

for i in dummy_data.dummy_statuses():
    database_queries.populate_statuses(i)

for i in dummy_data.dummy_person_skills():
    database_queries.insert_person_skills(i)

for i in dummy_data.dummy_jobs():
    database_queries.create_job(i)

# code to generate dummy jobs
# for i in dummy_data.dummy_jobs_many(100):
#     database_queries.create_job(i)
