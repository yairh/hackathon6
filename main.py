import os
from bottle import (get, post, redirect, request, route, run, static_file, error, template)
import utils
import mysql.connector
from conf import username, pw, prt, database
import logging

# Static Routes t


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


    @route('/show/<showid>')
    def browse_show(showid):
        sectionTemplate = "./templates/show.tpl"
        sectionData = utils.getJsonFromFile(int(showid))
        if showid not in utils.AVAILABE_SHOWS:
            return error404(error)
        else:
            return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


    # @route('/ajax/show/<catid>')
    # def browse_skills_from(catid):
    #     try:
    #         con = mysql.connector.connect(user=username, password=pw, database=database, port=prt)
    #         cur = con.cursor()
    #
    #         cur.execute(
    #             """
    #             SELECT *
    #             FROM skill_categories
    #             """)
    #
    #         result = cur.fetchall()
    #         return result
    #     except Exception as err:
    #         logging.exception(err)
    #     con.close()
    #     return template("./templates/show.tpl", result=result)


    @route('/show/<showid>/episode/<episodeid>')
    def browse_show(showid, episodeid):
        sectionTemplate = "./templates/episode.tpl"
        result = utils.getJsonFromFile(int(showid))
        for ep in result['_embedded']['episodes']:
            if ep["id"] == int(episodeid):
                sectionData = ep
            else:
                return error404(error)
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=sectionData)


    @route('/ajax/show/<showid>/episode/<episodeid>')
    def browse_show(showid, episodeid):
        data = utils.getJsonFromFile(int(showid))
        for ep in data['_embedded']['episodes']:
            if ep["id"] == int(episodeid):
                result = ep
        return template("./templates/episode.tpl", result=result)


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
        print(result)
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={}, query=query, results=results)


    @get('/profile')
    def get_profile():
        sectionTemplate = "./templates/profile.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


    @post('/profile')
    def update_profile():
        sectionTemplate = "./templates/profile.tpl"
        result = {
            "name": request.forms.get("name"),
            "skill": request.forms.get("skill"),
            "city": request.forms.get("city")
        }
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


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
        print(result)
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


    @error(404)
    def error404(error):
        sectionTemplate = "./templates/404.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


    # run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
    run(host='localhost', port=7000)
