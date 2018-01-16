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

@app.route('/start', methods=['GET', 'POST'])
def start_prog():
    # TODO get request params
    height = request.form('height')
    width = request.form('width')
    game_id = request.form('game_id')
    is_json_type = request.is_json


    return """
    <div>ISJSON is {jsonify}</div>
    <div>WIDTH is {width}</div>
    <div>HEIGHT: is {height}</div>
    <div>language is {game_id}</div>
    """.format(jsonify=is_json_type, width=width, height=height, game_id=game_id)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
