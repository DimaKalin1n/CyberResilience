from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)

r = Redis(host='127.0.0.1', port='6379')


@app.route('/visit/<user_name>')
def homePage(user_name):
    r.incr(user_name)
    return 'ok'


@app.route('/visit/show')
def show_page():
    str1 = r.keys()
    return str(len(str1))


@app.route('/show/<user_name>')
def show(user_name):
    return r.get(user_name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)