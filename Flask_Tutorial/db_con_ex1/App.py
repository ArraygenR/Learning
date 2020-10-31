from flask import Flask , render_template , request
from flask_mysqldb import  MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test1'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        sql = "INSERT INTO `tblUser` (`fname`, `lname`) VALUES (\'"+firstName+"\',\'"+lastName+"\')"
        print(sql)
        cur = mysql.connection.cursor()
        cur.execute(sql)       
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)


"""
Top Stop Existing running server
ps -fA | grep python
check id and
kill -9 6209/this is id
and rerun code
"""