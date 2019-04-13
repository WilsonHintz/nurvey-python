import datetime
import numpy
from loadModel import loadModel
from loggerFile import loggerFile
from flask import Flask, render_template
from flask import request, jsonify
import json

app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': 'Json de prueba',
        'description': u'objeto',
        'done': True
    }
]

network_output = {
        "date": "2018-11-11",
        "result": "Json de prueba",
        "networkName": "default",
        "networkVersion": "1"
}

responses = 0


@app.route('/')
def homepage():
    the_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    return """
    <h1>Neural Server</h1>
    <p>Hour: {time}.</p>
    <p>2 models serving</p>
    <p>Responses until now: {RespCount}</p>

    <img src="https://i.imgur.com/nxQphlD.jpg">
    """.format(time=the_time, RespCount=responses)


@app.route('/main')
def mainpage():
    return render_template("index.html")


@app.route('/object', methods=['GET'])
def rest():
    return jsonify({'tasks': tasks})


@app.route('/postjson', methods=['POST'])
def postJsonHandler():
    global responses
    print("===========")
    print(request.is_json)
    content = request.get_json()
    print(content['x'])
    loggerFile.INPUT(str(content['x']))

    dataset = numpy.fromstring(content['x'], sep=",")
    dataset2 = numpy.vstack([dataset, dataset])
    salida = loaded_model.predict(dataset2[:, 0:14])

    print("salida")
    i, j = numpy.unravel_index(salida.argmax(), salida.shape)
    print("categoria" + categoriaNSE(j))

    # RESPONSE BUILD ======
    network_output["date"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    network_output["result"] = str(categoriaNSE(j))
    network_output["networkName"] = "NSE vector 14"
    network_output["networkVersion"] = "1"

    loggerFile.OUTPUT(str(network_output))
    responses += 1
    print("total inf: " + str(responses))
    print("===========")

    return json.dumps(network_output, indent=4), 200


@app.route('/postjsonModel2', methods=['POST'])
def postJson2Handler():
    global responses
    print("===========")
    print(request.is_json)
    content = request.get_json()
    print(content['x'])

    dataset = numpy.fromstring(content['x'], sep=",")
    dataset2 = numpy.vstack([dataset, dataset])
    salida = loaded_model2.predict(dataset2[:, 0:24])

    print("salida")
    i, j = numpy.unravel_index(salida.argmax(), salida.shape)
    print("categoria" + categoriaNSE(j))

    # RESPONSE BUILD ======
    network_output["date"] = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    network_output["result"] = str(categoriaNSE(j))
    network_output["networkName"] = "NSE vector 24"
    network_output["networkVersion"] = "1"

    loggerFile.OUTPUT(str(network_output))
    responses += 1
    print("total inf: " + str(responses))
    print("===========")

    return json.dumps(network_output, indent=4), 200


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


if __name__ == "__main__":
    # start the web server
    print("* Starting web service...")
    # loadModel()
    global loaded_model
    loaded_model = loadModel.get_loadedmodel()
    global loaded_model2
    loaded_model2 = loadModel.get_loadedmodel2()
    loggerFile.INFO("------------")
    loggerFile.INFO("Server Start")
    loggerFile.INFO("------------")

    app.run(host='0.0.0.0', port=5000, debug=False, threaded=False)


