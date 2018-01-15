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

@app.route('/start')
def start_prog():
    # TODO get request params
    height = 3
    return """
    <div>{params}</div>
    """.format(params=height)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
