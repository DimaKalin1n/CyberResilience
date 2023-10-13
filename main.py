from flask import Flask
from redis import Redis
from dotenv import load_dotenv, dotenv_values


app = Flask(__name__)

load_dotenv()
env = dotenv_values('.env')

r = Redis(host='redis', port=env['REDIS_PORT'])


@app.route('/docker build -t my_flask_app:v0.1 my_flask_app/')
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
    app.run(host=env['FLASK_HOST'], debug=env['DEBUG'], port=env['FLASK_PORT'])