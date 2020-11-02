from flask import Flask
from flask import render_template
from db import mysql

app = Flask(__name__)
db = mysql.Testdb()

@app.route("/")
def hello():
    result = db.select_all()
    return str(result)

@app.route("/abc")
def hello2():
    a = "{1:aa,2:bb}"
    return a

@app.route("/univ/<aaa>")
def hello3(aaa):
    a = aaa
    return a

@app.route("/message/<string:message_id>")
def get_message(message_id):
    print(type(message_id))
    return "message id: %s" % message_id

@app.route("/first/<int:messageid>")
def get_first(messageid):
    print(type(messageid))
    return "<h1>%d</h1>" % (messageid + 5)

@app.route('/<user>')
def test(user):
   return user
#
@app.route("/test")
def get_html():
    return render_template("view.html", aa='전달데이터',bb="1234",cc=[1,2,3])
#
@app.route('/hello/<user>')
def hello_name(user):
   return render_template('view.html', data=user,list=[1,2,3,4])

@app.route("/index")
def index():
    result = db.select_all()
    return render_template("index.html",aaa=str(result))

if __name__ == "__main__":
    app.run()