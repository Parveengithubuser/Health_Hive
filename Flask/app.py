from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
        
def insertdb (conn,name,mobile,email,specialist,problem):
    sql= "INSERT into APPOINTMENT VALUES('{}','{}','{}','{}','{}')".format(name,mobile,email,specialist,problem)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bcw97627;PWD=uA6r9OTuX4lZUOCC",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/appointments')
def appointments():
    return render_template('Medicines.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/make', methods=['POST','GET'])
def make():
    if request.method == "POST":
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        specialist = request.form['specialist']
        problem = request.form['problem']
        insertdb(conn,name,mobile,email,specialist,problem)
        return render_template('contact.html')
        




if __name__ =='__main__':
    app.run( debug = True)
