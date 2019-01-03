from classes import *
from workflow import *

# query available job
#
# user1 = query_profile(1)
# user2 = query_profile(2)
# print(user1)

new_job_test_data = {'username': 'Ari', 'skill': 'Professional Wizard', 'worker_name': 'Yair'}

print('****************************************************************************************************\n')
print('Ari needs Yair to make some wizardly Neural Net magic. So Ari goes on Shareece and Creates a new Job.')
input('Press any key to continue: ')
print('Creating a new Job...')
new_job(new_job_test_data)
job = query_job(13)
print('****************************************************************************************************\n')
print('Now, a new job is created on the Shareece platform.')
print('Status: ', job.status)
print('Job Id: ', job.id)

print('****************************************************************************************************\n')
print("Yair takes his Deep Learning wand and comes to Ari's place to cast some magic\n")
input('Press any key to continue...')

shake_dic_test = dict(job_id=13)
for stat in range(5):
    if stat == 0:
        input('Begin handshake: To begin the job press any key...\n')
    if stat == 1:
        input('Begin handshake, To accept work press any key...\n')
    if stat == 2:
        input('End handshake, Job is finished ? press any key to continue...\n')
    if stat == 3:
        input('End handshake, Finished the Job ? press any key to continue...\n')

    if job.status == 'Complete':
        print('Job is Complete ! Neural Net wins !')
        break
    handshake(shake_dic_test)
    job = query_job(13)
    print('Job Status: ', job.status)
