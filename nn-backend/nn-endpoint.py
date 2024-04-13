import io
import flask
import cairosvg
import numpy as np
from flask_cors import CORS
from PIL import Image
from nn import Network # TODO: IMPORT MODEL HERE
from helper import shift_vector
from pathlib import Path

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

path = Path(__file__).parent / "data"

MODEL_PARAMS = [784, 10] #TODO: Change to match your model parameters
mnist = Network(MODEL_PARAMS, "data/mnist_weights.npy", "data/mnist_biases.npy", load_existing=True)

@app.route("/api/", methods=['GET'])
def index():
    response = flask.jsonify({"endpoints": ["/api/query_mnist/"]})
    return response

@app.route("/api/query_cc", methods=['GET'])
def query_cc():
    randi = np.random.randint(0, cc_data.shape[0])
    x_train = cc_norm_data[randi]
    x = cc_data[randi]
    # print(x)
    y_pred, _, _ = cc.forward(x_train)
    y_pred = np.argmax(y_pred)
    if (y_pred == 1):
        y_pred = "Fraud"
    else:
        y_pred = "Valid"
    date = random_date()
    response = flask.jsonify({"fraud": y_pred, "amount": x[-1], "name": censusname.generate(), "date": date})
    return response