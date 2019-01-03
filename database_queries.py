import logging
import mysql.connector

from conf import username, pw, prt, database

logger = logging.getLogger(__name__)


def create_databases(username=username, pw=pw, prt=prt, database=database):
    make_database(username, pw, prt, database)
    make_tables(username, pw, prt, database)
    logging.info('Complete database initialized.')


def make_database(username, pw, prt, database):
    con = mysql.connector.connect(user=username, password=pw, port=prt)
    cur = con.cursor()
    try:
        cur.execute(
                    """
                    CREATE DATABASE IF NOT EXISTS %s
                    """ % (database,))

        logging.info('Database started.')
    except Exception as err:
        logging.exception(err)
    con.close()


def make_tables(username, pw, prt, database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS cities
                (id int NOT NULL AUTO_INCREMENT,
                city varchar(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
                )
            """)

        logging.info('"cities" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS available_hobbies
                (id int NOT NULL AUTO_INCREMENT,
                hobby varchar(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
                )
            """)

        logging.info('"available_hobbies" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS available_languages
                (id int NOT NULL AUTO_INCREMENT,
                language varchar(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
                )
            """)

        logging.info('"available_languages" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users
                (id int NOT NULL AUTO_INCREMENT,
                username varchar(255) NOT NULL UNIQUE,
                image varchar(255),
                city_id int NOT NULL,
                age int DEFAULT NULL,
                children int DEFAULT NULL,
                wallet FLOAT NOT NULL DEFAULT 0,
                joined DATETIME DEFAULT now(),
                PRIMARY KEY (id),
                FOREIGN KEY (city_id) REFERENCES cities(id)
                )
            """)

        logging.info('"users" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS hobbies
                (id int NOT NULL AUTO_INCREMENT,
                user_id int NOT NULL,
                hobby_id int NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (hobby_id) REFERENCES available_hobbies(id)
                )
            """)

        logging.info('"hobbies" table initialized.')


        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS languages
                (id int NOT NULL AUTO_INCREMENT,
                user_id int NOT NULL,
                language_id int NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (language_id) REFERENCES available_languages(id)
                )
            """)

        logging.info('"languages" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS skill_categories
                (id int NOT NULL AUTO_INCREMENT,
                skill_category varchar(255) NOT NULL UNIQUE,
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
            CREATE TABLE IF NOT EXISTS statuses
                (id int NOT NULL AUTO_INCREMENT,
                status varchar(255) NOT NULL UNIQUE,
                PRIMARY KEY (id)
                )
            """)

        logging.info('"statuses" table initialized.')

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS jobs
                (id int NOT NULL AUTO_INCREMENT,
                user_id int NOT NULL,
                worker_id int DEFAULT NULL,
                skill_id int NOT NULL,
                status int NOT NULL,
                post_time DATETIME DEFAULT now(),
                start_time DATETIME DEFAULT NULL,
                complete_time DATETIME DEFAULT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (skill_id) REFERENCES skills(id),
                FOREIGN KEY (status) REFERENCES statuses(id)
                )
            """)

        logging.info('"jobs" table initialized.')

    except Exception as err:
        logging.exception(err)
    con.close()


def populate_cities(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['city']]
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        try:
            the_query = """
                INSERT INTO cities (
                    city
                ) VALUES (%s)
                """

            cur.execute(the_query, insert_string)
            con.commit()
        except mysql.connector.IntegrityError as err:
            # 1062 is raised when there is an attempt to perform a duplicate entry into a column with a unique flag
            if not err.errno == 1062:
                raise
    except Exception as err:
        logging.exception(err)
    con.close()


def populate_hobbies(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['hobby']]
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        try:
            the_query = """
                INSERT INTO available_hobbies (
                    hobby
                ) VALUES (%s)
                """

            cur.execute(the_query, insert_string)
            con.commit()
        except mysql.connector.IntegrityError as err:
            # 1062 is raised when there is an attempt to perform a duplicate entry into a column with a unique flag
            if not err.errno == 1062:
                raise
    except Exception as err:
        logging.exception(err)
    con.close()


def populate_languages(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['language']]
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        try:
            the_query = """
                INSERT INTO available_languages (
                    language
                ) VALUES (%s)
                """

            cur.execute(the_query, insert_string)
            con.commit()
        except mysql.connector.IntegrityError as err:
            # 1062 is raised when there is an attempt to perform a duplicate entry into a column with a unique flag
            if not err.errno == 1062:
                raise
    except Exception as err:
        logging.exception(err)
    con.close()


def populate_skill_categories(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['skill_category'], details['image']]

    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        try:

            the_query = """
                INSERT INTO skill_categories (
                    skill_category,
                    image
                ) VALUES (%s, %s)
                """

            cur.execute(the_query, insert_string)
            con.commit()
        except mysql.connector.IntegrityError as err:
            # 1062 is raised when there is an attempt to perform a duplicate entry into a column with a unique flag
            if not err.errno == 1062:
                raise

    except Exception as err:
        logging.exception(err)
    con.close()


def populate_skills(details, username=username, pw=pw, prt=prt, database=database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        try:
            cur.execute(
                """
                SELECT id
                FROM skill_categories
                WHERE skill_category='%s'
                """ % (details['skill_category'],))

            result = cur.fetchall()

            insert_string = [result[0][0], details['skill'], details['image']]

            the_query = """
                INSERT INTO skills (
                    category,
                    skill,
                    image
                ) VALUES (%s, %s, %s)
                """

            cur.execute(the_query, insert_string)
            con.commit()
        except mysql.connector.IntegrityError as err:
            # 1062 is raised when there is an attempt to perform a duplicate entry into a column with a unique flag
            if not err.errno == 1062:
                raise
    except Exception as err:
        logging.exception(err)
    con.close()


def populate_statuses(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['status']]

    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        try:
            the_query = """
                INSERT INTO statuses (
                    status
                ) VALUES (%s)
                """

            cur.execute(the_query, insert_string)
            con.commit()
        except mysql.connector.IntegrityError as err:
            # 1062 is raised when there is an attempt to perform a duplicate entry into a column with a unique flag
            if not err.errno == 1062:
                raise
    except Exception as err:
        logging.exception(err)
    con.close()


def populate_single_master(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = list(*details.items())

    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        the_query = """
            INSERT INTO %s (
                status
            ) VALUES (%s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def insert_user_details(details, username=username, pw=pw, prt=prt, database=database):
    populate_cities(details)

    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:
        try:
            cur.execute(
                """
                SELECT id
                FROM cities
                WHERE city='%s'
                """ % (details['city'],))

            the_city = cur.fetchall()

            insert_string = [details['username'], details['image'], the_city[0][0]]

            the_query = """
                INSERT INTO users (
                    username,
                    image,
                    city_id
                ) VALUES (%s, %s, %s)
                """

            cur.execute(the_query, insert_string)
            con.commit()
        except mysql.connector.IntegrityError as err:
            # 1062 is raised when there is an attempt to perform a duplicate entry into a column with a unique flag
            if not err.errno == 1062:
                raise

    except Exception as err:
        logging.exception(err)
    con.close()


def update_age(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['age'], details['username']]
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:


        the_query = """
            UPDATE users
            SET age=%s
            WHERE username=%s
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def update_children(details, username=username, pw=pw, prt=prt, database=database):
    insert_string = [details['children'], details['username']]
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    cur = con.cursor()
    try:


        the_query = """
            UPDATE users
            SET children=%s
            WHERE username=%s
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def insert_person_skills(details, username=username, pw=pw, prt=prt, database=database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)

    cur = con.cursor()
    try:
        cur.execute(
            """
            SELECT id
            FROM users
            WHERE username='%s'
            """ % (details['username'],))

        the_username = cur.fetchall()

        cur.execute(
            """
            SELECT id
            FROM skills
            WHERE skill='%s'
            """ % (details['skill'],))

        the_skill = cur.fetchall()

        insert_string = [the_username[0][0], the_skill[0][0]]

        the_query = """
            INSERT INTO person_skills (
                user_id,
                skill_id
            ) VALUES (%s, %s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def insert_language(details, username=username, pw=pw, prt=prt, database=database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)

    cur = con.cursor()
    try:
        cur.execute(
            """
            SELECT id
            FROM users
            WHERE username='%s'
            """ % (details['username'],))

        the_username = cur.fetchall()

        cur.execute(
            """
            SELECT id
            FROM available_languages
            WHERE language='%s'
            """ % (details['language'],))

        the_language = cur.fetchall()

        insert_string = [the_username[0][0], the_language[0][0]]

        the_query = """
            INSERT INTO languages (
                user_id,
                language_id
            ) VALUES (%s, %s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


def insert_hobby(details, username=username, pw=pw, prt=prt, database=database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)

    cur = con.cursor()
    try:
        cur.execute(
            """
            SELECT id
            FROM users
            WHERE username='%s'
            """ % (details['username'],))

        the_username = cur.fetchall()

        cur.execute(
            """
            SELECT id
            FROM available_hobbies
            WHERE hobby='%s'
            """ % (details['hobby'],))

        the_language = cur.fetchall()

        insert_string = [the_username[0][0], the_language[0][0]]

        the_query = """
            INSERT INTO hobbies (
                user_id,
                hobby_id
            ) VALUES (%s, %s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()

def create_job(details, username=username, pw=pw, prt=prt, database=database):
    con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)

    cur = con.cursor()
    try:
        cur.execute(
            """
            SELECT id
            FROM users
            WHERE username='%s'
            """ % (details['username'],))

        the_username = cur.fetchall()

        cur.execute(
            """
            SELECT id
            FROM skills
            WHERE skill='%s'
            """ % (details['skill'],))

        the_skill = cur.fetchall()

        cur.execute(
            """
            SELECT id
            FROM statuses
            WHERE status='Available'
            """)

        the_status = cur.fetchall()

        insert_string = [the_username[0][0], the_skill[0][0], the_status[0][0]]

        the_query = """
            INSERT INTO jobs (
                user_id,
                skill_id,
                status
            ) VALUES (%s, %s, %s)
            """

        cur.execute(the_query, insert_string)
        con.commit()
    except Exception as err:
        logging.exception(err)
    con.close()


if __name__ == "__main__":
    # pass
    # create_databases()
    #
    import dummy_data

    # for i in dummy_data.dummy_user_details():
    #     insert_user_details(i)
    #
    # for i in dummy_data.dummy_skill_categories():
    #     populate_skill_categories(i)
    #
    # for i in dummy_data.dummy_skills():
    #     populate_skills(i)
    #
    # for i in dummy_data.dummy_statuses():
    #     populate_statuses(i)
    #
    # for i in dummy_data.dummy_person_skills():
    #     insert_person_skills(i)
    #
    # for i in dummy_data.dummy_jobs():
    #     create_job(i)
