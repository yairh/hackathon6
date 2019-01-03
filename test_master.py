import sys
import logging

import dbflag

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

if dbflag.check_if_the_db_exists() is False:
    import database_queries
    import dummy_data

    database_queries.create_databases()

    for i in dummy_data.dummy_languages():
        database_queries.populate_languages(i)

    for i in dummy_data.dummy_hobbies():
        database_queries.populate_hobbies(i)

    for i in dummy_data.dummy_user_details():
        database_queries.insert_user_details(i)

    for i in dummy_data.dummy_user_details():
        database_queries.insert_hobby(i)

    for i in dummy_data.dummy_user_details():
        database_queries.insert_language(i)

    for i in dummy_data.dummy_user_details():
        database_queries.update_age(i)

    for i in dummy_data.dummy_user_details():
        database_queries.update_children(i)

    for i in dummy_data.dummy_skill_categories():
        database_queries.populate_skill_categories(i)

    for i in dummy_data.dummy_skills():
        database_queries.populate_skills(i)

    for i in dummy_data.dummy_statuses():
        database_queries.populate_statuses(i)

    for i in dummy_data.dummy_person_skills():
        database_queries.insert_person_skills(i)

    # for i in dummy_data.dummy_jobs():
    #     database_queries.create_job(i)

    logging.info('Database populated.')

if __name__ == "__main__":
    import main
    main.main()


# code to generate dummy jobs
# for i in dummy_data.dummy_jobs_many(100):
#     database_queries.create_job(i)
