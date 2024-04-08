import flask
from flask_cors import CORS
from PIL import Image
import cairosvg
import numpy as np
import io
from nn import Network
from helper import shift_vector
import pandas as pd
from pathlib import Path

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

path = Path(__file__).parent / "data"
nid_data = pd.read_csv(path / "clean_packet_data.csv")
nid_data = np.array(nid_data.drop(['id', 'class'], axis=1))

mnist = Network([784,700,500,300,10], "data/mnist_weights.npy", "data/mnist_biases.npy", load_existing=True)
# cc = Network([784,700,500,300,10], "data/mnist_weights.npy", "data/mnist_biases.npy", load_existing=True)
nid = Network([41,32,23], "data/nid_weights.npy", "data/nid_biases.npy", load_existing=True)

@app.route("/api/", methods=['GET'])
def index():
    response = flask.jsonify({"endpoints": ["/api/query_mnist/", "/api/train_mnist"]})
    return response

@app.route("/api/query_mnist", methods=['POST'])
def query_mnist():
    mnist_svg = flask.request.get_json()["mnist_svg"]
    mem = io.BytesIO()
    cairosvg.svg2png(mnist_svg, output_width=28, output_height=28, write_to=mem, negate_colors=True)

    x = np.array(Image.open(mem))

    # Only consider first three channels (r,g,b), then convert to grayscale
    x = x[:,:,:3]
    x = x.mean(axis=2)

    # Calculate center of mass to center images
    center_x = np.argmax(x.mean(axis=1))
    center_y = np.argmax(x.mean(axis=0))
    x = shift_vector(x, center_x, center_y, 28, 28)

    # Flatten image, normalize
    x = x.flatten().reshape(784, 1)
    x = x / 255

    # Generate prediction
    y_pred, _, _ = mnist.forward(x)
    # print(y_pred)
    response = flask.jsonify({"0": str(y_pred[0][0]),
                              "1": str(y_pred[1][0]),
                              "2": str(y_pred[2][0]),
                              "3": str(y_pred[3][0]),
                              "4": str(y_pred[4][0]),
                              "5": str(y_pred[5][0]),
                              "6": str(y_pred[6][0]),
                              "7": str(y_pred[7][0]),
                              "8": str(y_pred[8][0]),
                              "9": str(y_pred[9][0])})
    return response

@app.route("/api/query_cc", methods=['POST'])
def query_cc():
    mnist_svg = flask.request.get_json()["mnist_svg"]
    mem = io.BytesIO()
    cairosvg.svg2png(mnist_svg, output_width=28, output_height=28, write_to=mem, negate_colors=True)
    x = np.array(Image.open(mem))
    x = x[:,:,:3]
    x = x.mean(axis=2)
    x = x.flatten().reshape(784, 1)
    x = x / 255
    # print(x)
    y_pred, _, _ = mnist.forward(x)
    y_pred = np.argmax(y_pred)
    print(y_pred)
    response = flask.jsonify({"pred": str(y_pred)})
    return response

@app.route("/api/query_nid", methods=['GET'])
def query_nid():
    x = nid_data[np.random.randint(0, nid_data.shape[0])]
    y_pred, _, _ = nid.forward(x)
    y_pred = np.argmax(y_pred)
    out = {'duration': x[0], 'protocol_type': x[1], 'service': x[2], 'flag': x[3], 'src_bytes': x[4],
       'dst_bytes': x[5], 'land': x[6], 'wrong_fragment': x[7], 'urgent': x[8], 'hot': x[9],
       'num_failed_logins': x[10], 'logged_in': x[11], 'num_compromised': x[12], 'root_shell': x[13],
       'su_attempted': x[14], 'num_root': x[15], 'num_file_creations': x[16], 'num_shells': x[17],
       'num_access_files': x[18], 'num_outbound_cmds': x[19], 'is_host_login': x[20],
       'is_guest_login': x[21], 'count': x[22], 'srv_count': x[23], 'serror_rate': x[24],
       'srv_serror_rate': x[25], 'rerror_rate': x[26], 'srv_rerror_rate': x[27], 'same_srv_rate': x[28],
       'diff_srv_rate': x[29], 'srv_diff_host_rate': x[30], 'dst_host_count': x[31],
       'dst_host_srv_count': x[32], 'dst_host_same_srv_rate': x[33],
       'dst_host_diff_srv_rate': x[34], 'dst_host_same_src_port_rate': x[35],
       'dst_host_srv_diff_host_rate': x[36], 'dst_host_serror_rate': x[37],
       'dst_host_srv_serror_rate': x[38], 'dst_host_rerror_rate': x[39],
       'dst_host_srv_rerror_rate': x[40], "pred": str(y_pred)}
    response = flask.jsonify(out)

    
    return response

# @app.route("/api/train_mnist", methods=['POST'])
# def train_mnist():
#     sizes = [784].extend(custom_sizes)
#     sizes.extend(10)
#     model = Network(sizes)
#     model.sgd_train(X_train, Y_train, X_test, Y_test, epochs=30, batch_size=1024, lr=0.1, verbose=True)

#     return