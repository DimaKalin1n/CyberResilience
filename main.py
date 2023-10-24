from flask import Flask
from redis import Redis
from dotenv import load_dotenv, dotenv_values


app = Flask(__name__)


load_dotenv()
env = dotenv_values('.env')


r = Redis(host='redis', port=env['REDIS_PORT'])


@app.route('/<user_name>')
def home_page(user_name):
    '''Добавлению пользвателя'''
    r.incr(user_name)
    return 'ok'


@app.route('/visit/show')
def show_page():
    '''Показать кол-во юзеров'''
    str1 = r.keys()
    return str(len(str1))


@app.route('/show/<user_name>')
def show(user_name):
    '''Порядковый номер'''
    return r.get(user_name)


if __name__ == '__main__':
    app.run(host=env['FLASK_HOST'], debug=env['DEBUG'], port=env['FLASK_PORT'])
