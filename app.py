import datetime
import numpy
from loadModel import loadModel
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
loaded_model = None
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
    the_time = datetime.datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="https://i.imgur.com/nxQphlD.jpg">
    """.format(time=the_time)


@app.route('/dollyPuto', methods=['GET'])
def rest():
    return jsonify({'tasks': tasks})


@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    print(request.is_json)
    content = request.get_json()
    print(content['x'])

    dataset = numpy.fromstring(content['x'], sep=",")
    dataset2 = numpy.vstack([dataset, dataset])
    salida = loaded_model.predict(dataset2[:, 0:14])

    print("")
    print("salida")
    i, j = numpy.unravel_index(salida.argmax(), salida.shape)
    print("categoria")
    categoriaNSE(j)
    print(categoriaNSE(j))
    data = {'Categoria': categoriaNSE(j)}

    #return 'Categoria ' + categoriaNSE(j)
    return jsonify(data), 200


def categoriaNSE(nivel):
    return {
        0: "E",
        1: "E",
        2: "D2",
        3: "D1",
        4: "C3",
        5: "C2",
        6: "C1",
        7: "AB"
    }.get(nivel, "error")

# def loadModel():
#     json_file = open('./models/modelNoBin.json', 'r')
#     loaded_model_json = json_file.read()
#     json_file.close()
#     global loaded_model
#     loaded_model = model_from_json(loaded_model_json)
#     # load weights into new model
#     loaded_model.load_weights("./models/modelNoBin.h5")
#
#     print("Loaded model from disk")


if __name__ == "__main__":
    # start the web server
    print("* Starting web service...")
    # loadModel()
    loaded_model = loadModel.get_loadedmodel()
    app.run(debug=True, threaded=False, use_reloader=True)
