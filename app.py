from flask import Flask, request
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

@app.route('/start' methods=['GET', 'POST'])
def start_prog():
    data = request.args
    # TODO get request params
    language = data.get('language')
    height = data.get('height')
    width = data.get('width')
    game_id = data.get('game_id')

    return """
    <div>Method is {meth_get}</div>
    <div>language is {params}</div>
    <div>language is {height}</div>
    <div>language is {width}</div>
    <div>language is {game_id}</div>
    """.format(meth_get=request.method, params=language, height=height, width=width, game_id=game_id)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
