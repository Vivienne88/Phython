from flask import Flask, url_for, redirect
app = Flask(__name__)

#웹 루트 접속했을 때
@app.route('/')
#Hello World함수 호출
def hello_world():
   return redirect(url_for('login'))

@app.route('/login/')
def login():
    return 'login'

@app.route('/profile/<username>')
def get_profile(username):
    return 'profile : ' + username

@app.route('/message/<int:message_id>')
def get_message(message_id):
    return 'message id : %d' % message_id

if __name__ == '__main__':
    app.debug = True
    app.run(host = '203.252.166.42')