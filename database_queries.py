import logging
import mysql.connector

from conf import username, pw, prt, database

logger = logging.getLogger(__name__)


def create_databases(username=username, pw=pw, prt=prt, database=database):
    make_database(username, pw, prt, database)
    make_tables(username, pw, prt, database)


def make_database(username, pw, prt, database):
    con = mysql.connector.connect(user=username, password=pw, port=prt)

    cur = con.cursor()
    try:
        cur.execute(
            """
            CREATE DATABASE IF NOT EXISTS %s
            """ % (database,))

        logging.info('Database initialized.')
    except Exception as err:
        logging.exception(err)
    con.close()


def make_tables(username, pw, prt, database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)

    cur = con.cursor()
    try:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users
                (id int NOT NULL AUTO_INCREMENT,
                username varchar(255) NOT NULL UNIQUE,
                wallet FLOAT NOT NULL DEFAULT 0,
                PRIMARY KEY (id)
                )
            """)

        logging.info('"users" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS skill_categories
                (id int NOT NULL AUTO_INCREMENT,
                skill_category varchar(255) NOT NULL,
                image varchar(255) DEFAULT NULL,
                PRIMARY KEY (id)
                )
            """)

        logging.info('"skill_categories" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS skills
                (id int NOT NULL AUTO_INCREMENT,
                category int NOT NULL,
                skill varchar(255) NOT NULL,
                image varchar(255) DEFAULT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (category) REFERENCES skill_categories(id)
                )
            """)

        logging.info('"skills" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS person_skills
                (id int NOT NULL AUTO_INCREMENT,
                user_id int NOT NULL,
                skill_id int NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (skill_id) REFERENCES skills(id)
                )
            """)

        logging.info('"person_skills" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS job_status
                (id int NOT NULL AUTO_INCREMENT,
                status varchar(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
                )
            """)

        logging.info('"job_status" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS available_jobs
                (id int NOT NULL AUTO_INCREMENT,
                user_id int NOT NULL,
                skill_id int NOT NULL,
                status int NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (skill_id) REFERENCES skills(id),
                FOREIGN KEY (status) REFERENCES job_status(id)
                )
            """)

        logging.info('"available_jobs" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS pending_jobs
                (id int NOT NULL AUTO_INCREMENT,
                applicant_id int NOT NULL,
                worker_id int NOT NULL,
                job_id int NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (applicant_id) REFERENCES users(id),
                FOREIGN KEY (worker_id) REFERENCES users(id),
                FOREIGN KEY (job_id) REFERENCES available_jobs(id)
                )
            """)

        logging.info('"pending_jobs" table initialized.')

    except Exception as err:
        logging.exception(err)
    con.close()


def populate_skill_categories(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['skill_category']]

    try:
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()

        the_query = """
            INSERT INTO skill_categories (
                skill_category
            ) VALUES (%s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def populate_skills(details, username=username, pw=pw, prt=prt, database=database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)

    cur = con.cursor()
    try:
        cur.execute(
            """
            SELECT id
            FROM skill_categories
            WHERE skill_category='%s'
            """ % (details['skill_category'],))

        result = cur.fetchall()

        insert_string = [result[0][0], details['skill']]

        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()

        the_query = """
            INSERT INTO skills (
                category,
                skill
            ) VALUES (%s, %s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def populate_job_status(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['status']]

    try:
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()

        the_query = """
            INSERT INTO job_status (
                status
            ) VALUES (%s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def insert_user_details(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['username']]

    try:
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()

        the_query = """
            INSERT INTO users (
                username
            ) VALUES (%s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


if __name__ == "__main__":
    # create_databases()

    import dummy_data

    # for i in dummy_data.dummy_user_details():
    #     insert_user_details(i)
    #
    # for i in dummy_data.dummy_skill_categories():
    #     populate_skill_categories(i)
    #
    # for i in dummy_data.dummy_skills():
    #     populate_skills(i)

    for i in dummy_data.dummy_job_status():
        populate_job_status(i)
