import sys
from workflow import *

job_id = 13


def job_demo(job_id):
    job = query_job(job_id)
    print(job)

    # first handshake
    confirm = input('Please hit a key to agree, hit [n/N] to refuse: ')
    if confirm == 'N' or confirm == 'n':
        print('Job stopped')
        sys.exit(0)
    else:
        job.start()
        print(job)
        print('Job started ! Waiting for second agreement')

    # second handshake
    confirm = input('Please hit a key to agree, hit [n/N] to refuse: ')
    if confirm == 'N':
        print('Job stopped')
        sys.exit(0)
    else:
        job.progress()
        print(job)
        print('Job in Progress ! Agreement reached !')

    # Third hanshake
    confirm = input('Please hit a key to agree, hit [n/N] to refuse: ')
    if confirm == 'N':
        print('Job stopped')
        sys.exit(0)
    else:
        job.finish()
        print(job)
        print('Job finished ! Waiting for second agreement !')

    # Fourth handshake
    confirm = input('Please hit a key to agree, hit [n/N] to refuse: ')
    if confirm == 'N':
        print('Job stopped')
        sys.exit(0)
    else:
        job.complete()
        print(job)
        print('Transaction Done ! Thank for using Shareece')


job_demo(job_id)
