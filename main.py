import os
from bottle import (get, post, redirect, request, route, run, static_file, error, template)
import utils
import mysql.connector
from conf import username, pw, prt, database
import logging
import workflow

def main():
    @get("/js/<filepath:re:.*\.js>")
    def js(filepath):
        return static_file(filepath, root="./js")


    @get("/css/<filepath:re:.*\.css>")
    def css(filepath):
        return static_file(filepath, root="./css")


    @get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
    def img(filepath):
        return static_file(filepath, root="./images")


    @route('/')
    def index():
        sectionTemplate = "./templates/home.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})


    @route('/browse')
    def redirect_browse():
        redirect("/browse/name")


    @route('/browse/<order>')
    def browse(order):
        sectionTemplate = "./templates/browse.tpl"
        # sectionData = utils.getListOfShows()
        sectionData = utils.getListOfSkills()
        if order == 'name':
            sectionData.sort(key=lambda x: x[1], reverse=False)
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


    # @route('/show/<showid>')
    # def browse_show(showid):
    #     sectionTemplate = "./templates/show.tpl"
    #     sectionData = utils.getJsonFromFile(int(showid))
    #     if showid not in utils.AVAILABE_SHOWS:
    #         return error404(error)
    #     else:
    #         return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


    @route('/ajax/show/<catid>')
    def browse_skills_from(catid):
        try:
            con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
            cur = con.cursor()

            cur.execute(
                """
                SELECT *
                FROM skills
                WHERE category = %s
                """ % (catid,))

            result = cur.fetchall()
            result_bis = [elmt[0] for elmt in result]


            cur.execute(
                """
                SELECT *
                FROM skill_categories
                WHERE id = %s
                """ % (catid,))

            nameOfCat = cur.fetchone()[1]

            result_bis = []
            for subtuple in result:
                result_bis.append(list(subtuple))

        except Exception as err:
            logging.exception(err)
        con.close()
        return template("./templates/show.tpl", result=result_bis, nameOfCat=nameOfCat)


    @route('/show/<catid>/episode/<skillid>')
    def browse_show_core_reg(catid, skillid):
        skillers, nameOfSkill = browse_show_backend(catid, skillid)

        skillers2 = []
        for subtuple in skillers:
            skillers2.append(list(subtuple))


        sectionTemplate = "./templates/episode.tpl"
        return template("./pages/index.html", version=utils.getVersion(), result=skillers2, sectionTemplate=sectionTemplate, nameOfSkill=nameOfSkill, sectionData=skillers)


    @route('/ajax/show/<catid>/episode/<skillid>')
    def browse_show_core_ajax(catid, skillid):
        skillers, nameOfSkill = browse_show_backend(catid, skillid)
        return template("./templates/episode.tpl", result=skillers, nameOfSkill=nameOfSkill)

    def browse_show_backend(catid, skillid):
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()
        try:

            cur.execute(
                """
                SELECT id, username 
                FROM users WHERE id 
                in (SELECT user_id from person_skills 
                WHERE skill_id= %s)
                """ % (skillid,))

            skillers = cur.fetchall()
            skillers = list(skillers)

            cur.execute(
                """
                SELECT skill
                FROM skills
                WHERE id = %s
                """ % (skillid,))

            nameOfSkill = cur.fetchone()[0]


        except Exception as err:
            logging.exception(err)
        con.close()
        return skillers, nameOfSkill


    @route('/search')
    def search():
        sectionTemplate = "./templates/search.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


    @post('/search')
    def post_search():
        sectionTemplate = "./templates/search_result.tpl"
        result = {
            "query": request.forms.get('skillsearch')
        }
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, query=query, results=results)


    @get('/profile')
    def get_profile():
        sectionTemplate = "./templates/profile.tpl"
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()
        try:
            cur.execute(
                """
                SELECT wallet
                FROM users 
                where users.id = %s
                """ % (2,))

            balance = cur.fetchone()[0]
            balance = int(balance)

        except Exception as err:
            logging.exception(err)
        con.close()
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, balance=balance, sectionData={})


    @get('/profile/<userid>')
    def get_skiller_profile(userid):
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()
        try:
            cur.execute(
                """
                SELECT username, city, skill
                FROM users 
                JOIN cities 
                ON users.city_id = cities.id
                JOIN person_skills 
                ON users.id = person_skills.user_id 
                join skills 
                on person_skills.skill_id = skills.id
                where users.id = %s
                limit 1;
                """ % (userid,))

            result = cur.fetchone()

        except Exception as err:
            logging.exception(err)
        con.close()
        sectionTemplate = "./templates/skillerProfile.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=result, result=result)


    @get('/ajax/profile/<userid>')
    def get_skiller_profile_ajax(userid):
        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()
        try:
            cur.execute(
                """
                SELECT username, city, skill
                FROM users 
                JOIN cities 
                ON users.city_id = cities.id
                JOIN person_skills 
                ON users.id = person_skills.user_id 
                join skills 
                on person_skills.skill_id = skills.id
                where users.id = %s
                limit 1;
                """ % (userid,))

            result = cur.fetchone()

        except Exception as err:
            logging.exception(err)
        con.close()
        sectionTemplate = "./templates/skillerProfile.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, result=result, sectionData=result)


    @get('/register')
    def get_register_page():
        sectionTemplate = "./templates/register.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


    @post('/register')
    def register():
        sectionTemplate = "./templates/register.tpl"
        result = {
            "name": request.forms.get("name"),
            "skill": request.forms.get("skill"),
            "city": request.forms.get("city")
        }
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

    @get('/request')
    def get_request_page():
        sectionTemplate = "./templates/request.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


    @get('/ajax/request')
    def get_request_page():
        sectionTemplate = "./templates/request.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, result={})

    @post('/handshake')
    def post_handshake():
        result = {
            "date": request.forms.get("date"),
            "message": request.forms.get("message"),
            "username": "Ilona",
            "skill": "Mathematics",
            "worker_name": "Yair"
        }
        workflow.new_job(result)
        sectionTemplate = "./templates/myShareeces.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, result=result, sectionData={})

    @get('/shareeces')
    def get_myshareeces_page():
        sectionTemplate = "./templates/MyShareeces.tpl"

        userid=2

        con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
        cur = con.cursor()
        try:

            cur.execute(
                """
                SELECT t1.username, t2.skill, jobs.id
                FROM jobs
                JOIN users as t1
                ON jobs.worker_id=t1.id
                JOIN skills as t2
                ON jobs.skill_id=t2.id
                WHERE jobs.user_id=%s
                AND jobs.worker_id is not NULL
                """ % (userid,))

            result = cur.fetchone()


        except Exception as err:
            logging.exception(err)
        con.close()
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, result=result[2], sectionData={})

    @get('/shareecees')
    def get_myshareeces_page():
        workflow.handshake(13)
        sectionTemplate = "./templates/MyShareeces.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, result={}, sectionData={})


    @error(404)
    def error404(error):
        sectionTemplate = "./templates/404.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


    # run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
    run(host='localhost', port=7000)
