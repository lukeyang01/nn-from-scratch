import flask
from flask_cors import CORS
import numpy as np
from nn import Network
import pandas as pd
from pathlib import Path
from sklearn import preprocessing

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

path = Path(__file__).parent / "data"
nid_data = pd.read_csv(path / "clean_packet_data.csv")
nid_data = np.array(nid_data.drop(['id', 'class'], axis=1))
nid_norm_data = preprocessing.normalize(nid_data)

MODEL_PARAMS = [41, 23] #TODO: Change to match your params
nid = Network([MODEL_PARAMS], "data/nid_weights.npy", "data/nid_biases.npy", load_existing=True)

@app.route("/api/", methods=['GET'])
def index():
    response = flask.jsonify({"endpoints": ["/api/query_nid"]})
    return response

@app.route("/api/query_nid", methods=['GET'])
def query_nid():
    randi = np.random.randint(0, nid_data.shape[0])
    x = nid_data[randi]
    x_train = nid_norm_data[randi]

    y_pred, _, _ = nid.forward(x_train)
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