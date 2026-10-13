#program for demonstrating connection from oracle DB

import oracledb as orc
try:
    kvr=orc.connect("system/tiger@localhost/orcl")
    print("python program obtain connection from oracle db")
    print("type of kvr=",type(kvr))
except orc.DatabaseError as db:
    print("Problem in oracle db:",db)