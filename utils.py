from bottle import template
import requests
import mysql.connector
import json
from conf import username, pw, prt, database
import logging


JSON_FOLDER = './data'
# AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871", "2993", "305"]
AVAILABE_SKILLS = ["coaching"]
URL_API = "http://api.tvmaze.com/shows/"


def getVersion():
    return "0.0.1"


def getJsonFromFile(showName):
    try:
        return json.loads(template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName)))

    except Exception as e:
        print(e)
        return "{}"


def getListOfSkills2():
# def getListOfShows():

    # result = [getJsonFromFile(x) for x in AVAILABE_SHOWS]
    result = [getJsonFromFile(x) for x in AVAILABE_SKILLS]
    return result


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
        print(result)
        return result
    except Exception as err:
        logging.exception(err)
    con.close()
