from flask import Flask

a = Flask(__name__)

@a.route('/sms1')

def lw():
    return "hello , i am om prakash kumar "

a.run(host="0.0.0.0")
~
