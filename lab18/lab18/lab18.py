from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
@app.route('/')
def hello(name = None) :
    data = [dict(href="http://www.naver.com",caption="네이버"), dict(href="http://www.google.com",caption="구글")]
    data2 = {
        'name' : 'SHY', 
        'skill' : 'Python'
    }
    #return render_template('hello.html',items = data, **data2)
    return render_template('main.html',items = data)
if __name__ == '__main__':
    #app.debug = True
    app.run();