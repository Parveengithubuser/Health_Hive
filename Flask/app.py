from flask import Flask,render_template,request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from BCW97627"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The Contact is : ", dictionary["MOBILE "])
        print("The Email  is : ",  dictionary["EMAIL"])
        print("The Specialist is : ",  dictionary["SPECIALIST"])
        print("The Problem is : ",  dictionary["PROBLEM"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(conn,name,contact,email,specialist,problem):
    sql= "select * from BCW97627 where name='{}',mobile number='{}',email='{}',specialist='{}' and problem='{}'".format(name,contact,email,specialist,problem)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The Mobile Number is : ", dictionary["MOBILE NUMBER"])
        print("The Email Id is : ",  dictionary["EMAIL ID"])
        print("The Specialist is : ",  dictionary["SPECIALIST"])
        print("The Problem is : ",  dictionary["PROBLEM"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,contact,email,specialist,problem):
    sql= "INSERT into BCW97627 VALUES('{}','{}','{}','{}','{}')".format(name,contact,email,specialist,problem)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bcw97627;PWD=uA6r9OTuX4lZUOCC",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template ('contact.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/Medicines')
def Medicines():
    return render_template('Medicines.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact.html', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        name = request.form['Name']
        contact = request.form['Mobile Number']
        email = request.form['Email id']
        specialist = request.form['Specialist']
        problem = request.form['Problem']
        
        #inp=[name,contact,email,address,specialist,problem]
        insertdb(conn,name,contact,email,specialist,problem)
        return render_template('contact.html')
        

@app.route('/contact.html', methods=['POST','GET'])
def contact():
    if request.method == "POST":
        name = request.form['Name']
        contact = request.form['Mobile Number']
        email = request.form['Email id']
        specialist = request.form['Specialist']
        problem = request.form['Problem']
        sql= "select * from Contact info where name='{}', mobile no='{}',email='{}',specialist=''{}',problem='{}'".format(name,contact,email,specialist,problem)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['contact'] =userdetails["EMAIL"]
            return ('contact.html',name==userdetails["NAME"],contact==userdetails["MOBILE"],email==userdetails["EMAIL"],specialist==userdetails["SPECIALIST"],problem==userdetails["PROBLEM"])
        else:
            msg = "Incorrect Email id or Password"
            return  ("contact.html", msg==msg)
    return render_template ('contact.html')


if __name__ =='__main__':
    app.run( debug = True)
