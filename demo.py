from classes import *
import sys
from workflow import *

job_id = 1


def job_demo(job_id):
    job = query_job(job_id)
    print(job)

    # first handshake
    confirm = input()
    if confirm == 'N':
        print('Job stopped')
        sys.exit(0)
    else:
        job.start()
        print(job)
        print('Job started ! Waiting for second agreement')

    # second handshake
    confirm = input()
    if confirm == 'N':
        print('Job stopped')
        sys.exit(0)
    else:
        job.progress()
        print(job)
        print('Job in Progress ! Agreement reached !')

    # Third hanshake
    confirm = input()
    if confirm == 'N':
        print('Job stopped')
        sys.exit(0)
    else:
        job.finish()
        print(job)
        print('Job finished ! Waiting for second agreement !')

    # Fourth handshake
    confirm = input()
    if confirm == 'N':
        print('Job stopped')
        sys.exit(0)
    else:
        job.complete()
        print(job)
        print('Transaction Done ! Thank for using Shareece')
