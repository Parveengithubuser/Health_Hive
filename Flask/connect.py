# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:58:50 2023

@author: Shivani_SB
"""
def showall():
    sql= "SELECT * from Contact info"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The Contact is : ", dictionary["MOBILE NUMBER"])
        print("The Email Id is : ",  dictionary["EMAIL ID"])
        print("The Specialist is : ",  dictionary["SPECIALIST"])
        print("The Problem is : ",  dictionary["PROBLEM"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(name,specialization):
    sql= "select * from Contact info where name='{}' and specialization='{}'".format(name,specialization)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The Contact is : ", dictionary["MOBILE NUMBER"])
        print("The Email Id is : ",  dictionary["EMAIL ID"])
        print("The Specialist is : ",  dictionary["SPECIALIST"])
        print("The Problem is : ",  dictionary["PROBLEM"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,contact,email,specialist,problem):
    sql= "INSERT into Contact info VALUES('{}','{}','{}','{}','{}')".format(name,contact,email,specialist,problem)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bcw97627;PWD=uA6r9OTuX4lZUOCC",'','')
    print(conn)
    print("connection successful...")
    #insertdb(conn,"Dr.K.Srinivas Reddy",)
    getdetails("Dr.K.Srinivas Reddy","Cardiologist")
    #showall()

except:
    print("Error connecting to the database")



