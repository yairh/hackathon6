import sys
import logging

from database_queries import create_databases, insert_user_details, populate_skill_categories, populate_skills

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

create_databases()

import dummy_data

for i in dummy_data.dummy_user_details():
    insert_user_details(i)

for i in dummy_data.dummy_skill_categories():
    populate_skill_categories(i)

for i in dummy_data.dummy_skills():
    populate_skills(i)