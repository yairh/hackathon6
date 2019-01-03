from database_queries import *
from classes import *


def new_user(user_dic):
    insert_user_details(user_dic)
    new_skill(user_dic)


def new_skill(user_dic):
    if isinstance(user_dic['skill'], str):
        user_dic['skill'] = [user_dic['skill']]

    for skill in user_dic['skill']:
        insert_person_skills(dict(username=user_dic['username'], skill=skill))


def new_job(job_dic):
    create_job(job_dic)
    update_worker(job_dic)


def handshake(shake_dic):
    job = query_job(shake_dic['job_id'])
    if job.status == 'Pending':
        job.start()
    elif job.status == 'Starting':
        job.progress()
    elif job.status == 'In Progress':
        job.finish()
    elif job.status == 'Finishing':
        job.complete()
