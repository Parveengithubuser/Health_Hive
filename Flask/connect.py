from flask import Flask, render_template, request,session

import ibm_db

def showall():
    sql = "SELECT * from Contact info"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The name is : ",  dictionary["name"])
        print("The mobile is : ", dictionary["mobile number"])
        print("The email is : ",  dictionary["email id"])
        print("The specialist is : ",  dictionary["specialist"])
        print("The Problem is : ",  dictionary[" prolem"])
        dictionary = ibm_db.fetch_both(stmt)

def insert_db(conn,name,mobile,email,specialist,problem):
    sql = "INSERT into APPOINTMENT VALUES('{}', '{}', '{}', '{}', '{}')".format(name,mobile,email,specialist,problem)
    stmt = ibm_db.exec_immediate(conn, sql)
    print("Number of affected rows: ", ibm_db.num_rows(stmt))

    

try:
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bcw97627;PWD=uA6r9OTuX4lZUOCC",'','')
    print(conn)
    print("Connection successful...")
    
    # Call the function to show all records
    showall()
 # Example of inserting a new record
    #insert_db(conn, "Cardiology", "Dr. Smith", "2023-08-26", "10:00 AM", "John Doe", 1234567890, "Heart issues")
    
   

except Exception as e:
    print("Error connecting to the database:", e)
