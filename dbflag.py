import logging
import mysql.connector

from conf import username, pw, prt, database

logger = logging.getLogger(__name__)

def check_if_the_db_exists(username=username, pw=pw, prt=prt, database=database):
    try:
        try:
            con = mysql.connector.connect(user=username, password=pw, port=prt, database=database)
            con.close()
        except mysql.connector.ProgrammingError as err:
            # 1049 is raised when the database that is being connected to doesn't exist
            if err.errno == 1049:
                return False
            else:
                raise
    except Exception as err:
        logging.exception(err)
    return True