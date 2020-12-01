from flask import Flask
from flask import request
from flask import render_template
from db import mysql

application = Flask(__name__)
# db = mysql.Testdb()

@application.route("/")
def hello():
    # result = db.select_all()
    return str("flask test")

@application.route("/abc")
def hello2():
    a = "{1:aa,2:bb}"
    return a

@application.route("/univ/<aaa>")
def hello3(aaa):
    a = aaa
    return a

@application.route("/message/<string:message_id>")
def get_message(message_id):
    print(type(message_id))
    return "message id: %s" % message_id

@application.route("/first/<int:messageid>")
def get_first(messageid):
    print(type(messageid))
    return "<h1>%d</h1>" % (messageid + 5)

@application.route('/<user>')
def test(user):
   return user
#
@application.route('/hello/<user>')
def hello_name(user):
   return render_template('view.html', data=user,list=[1,2,3,4])

@application.route("/index")
def index():
    # result = db.select_all()
    return render_template("index.html",aaa=str("aaa")


if __name__ == "__main__":
    application.debug = True
    application.config['DEBUG'] = True

    application.run(host="0.0.0.0", port="5000")