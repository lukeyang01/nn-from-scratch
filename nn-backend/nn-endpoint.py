import flask
from flask_cors import CORS
from PIL import Image
import cairosvg
import numpy as np
import io
from nn import Network
from helper import shift_vector

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mnist = Network([784,700,500,300,10], "data/mnist_weights.npy", "data/mnist_biases.npy", load_existing=True)

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

# @app.route("/api/train_mnist", methods=['POST'])
# def train_mnist():
#     sizes = [784].extend(custom_sizes)
#     sizes.extend(10)
#     model = Network(sizes)
#     model.sgd_train(X_train, Y_train, X_test, Y_test, epochs=30, batch_size=1024, lr=0.1, verbose=True)

#     return