import mysql.connector
from conf import username, pw, prt, database
import logging


AVAILABE_SKILLS = ["coaching"]
URL_API = "http://api.tvmaze.com/shows/"


def getVersion():
    return "0.0.1"


def getListOfSkills():
    try:
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()

        cur.execute(
            """
            SELECT *
            FROM skill_categories
            """)

        result = cur.fetchall()
        return result
    except Exception as err:
        logging.exception(err)
    con.close()
