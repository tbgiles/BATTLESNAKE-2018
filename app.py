from flask import Flask
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

@app.route('/testytesty')
def start_prog():
    test1 = {
    "width": 20
    "height":20
    "game_id": "blahblahblah"
    }
    # TODO get request params
    game_id = test1.args.get('game_id')
    height = test1.args.get('height')
    width = test1.args.get('width')
    return """
    <div>{params}</div>
    """.format(params=height)
    #{
    #"color" : #FF0000
    #"name" : "Daddy"
    #}

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
