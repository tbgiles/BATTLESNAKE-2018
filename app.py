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
    language = request.args.get('language')
    height = request.args.get('height')
    width = request.args.get('width')
    game_id = request.args.get('game_id')
    data = request.get_json(force=False, silent=False, cache=True)


    return """
    <div>Method is {meth_get}</div>
    <div>width is {params}</div>
    <div>Data is {data}</div>
    <div>language is {width}</div>
    <div>language is {game_id}</div>
    """.format(meth_get=request.method, params=width, data=data, width=width, game_id='asdhkj32408a')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
