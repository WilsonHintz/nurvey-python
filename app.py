from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': 'Gaston alonso',
        'description': u'persona, tagarna, alto petardo',
        'done': False
    }
]

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="https://i.imgur.com/nxQphlD.jpg">
    """.format(time=the_time)

@app.route('/dollyPuto', methods=['GET'])
def rest():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)