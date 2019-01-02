from hackathon6.transaction import *
from hackathon6.operations import *
import conf

# connect to fb
cnx = connect_todb(conf)

# query available job

user1 = query_profile(1, cnx)
user2 = query_profile(2, cnx)
