import flask
import censusname
import numpy as np
import pandas as pd
from sklearn import preprocessing
from flask_cors import CORS
from nn import Network # TODO: IMPORT MODEL HERE
from helper import random_date
from pathlib import Path

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

path = Path(__file__).parent / "data"

cc_data = pd.read_csv(path / "creditcard_2023.csv")
cc_data = np.array(cc_data.drop(['id', 'Class'], axis=1))
cc_norm_data = preprocessing.minmax_scale(cc_data)

MODEL_PARAMS = [29, 2] #TODO: Change to match your model parameters
cc = Network(MODEL_PARAMS, "data/cc_weights.npy", "data/cc_biases.npy", load_existing=True)

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