import io
import json
import os
import logging
import logging.config
import os
from JSONFormatter import JSONFormatter
from metrics import GaugeMetric, CounterMetric, start_metrics_server
from env import scope_keys, scope_values, app_name, prometheus_port
from env import request_count_metric

# Imports for the REST API
from flask import Flask, request, jsonify

# Imports for image procesing
from PIL import Image

# Imports for prediction
from predict import initialize, predict_image, predict_url

app = Flask(__name__)

# 4MB Max image size limit
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024



# Default route just shows simple text
@app.route('/')
def index():

    return 'MythicalScissorsObjDetection.ai model host harness'


# Like the CustomVision.ai Prediction service /image route handles either
#     - octet-stream image file
#     - a multipart/form-data with files in the imageData parameter
@app.route('/image', methods=['POST'])
@app.route('/<project>/image', methods=['POST'])
@app.route('/<project>/image/nostore', methods=['POST'])
@app.route('/<project>/classify/iterations/<publishedName>/image', methods=['POST'])
@app.route('/<project>/classify/iterations/<publishedName>/image/nostore', methods=['POST'])
@app.route('/<project>/detect/iterations/<publishedName>/image', methods=['POST'])
@app.route('/<project>/detect/iterations/<publishedName>/image/nostore', methods=['POST'])
def predict_image_handler(project=None, publishedName=None):
    try:
        imageData = None
        if ('imageData' in request.files):
            imageData = request.files['imageData']
        elif ('imageData' in request.form):
            imageData = request.form['imageData']
        else:
            imageData = io.BytesIO(request.get_data())

        logger.info("Request received")
        img = Image.open(imageData)
        results = predict_image(img)
        request_count_metric.inc(1, scope_values)
        return jsonify(results)
    except Exception as e:
        logger.exception(e)
        return 'Error processing image', 500


# Like the CustomVision.ai Prediction service /url route handles url's
# in the body of hte request of the form:
#     { 'Url': '<http url>'}
@app.route('/url', methods=['POST'])
@app.route('/<project>/url', methods=['POST'])
@app.route('/<project>/url/nostore', methods=['POST'])
@app.route('/<project>/classify/iterations/<publishedName>/url', methods=['POST'])
@app.route('/<project>/classify/iterations/<publishedName>/url/nostore', methods=['POST'])
@app.route('/<project>/detect/iterations/<publishedName>/url', methods=['POST'])
@app.route('/<project>/detect/iterations/<publishedName>/url/nostore', methods=['POST'])
def predict_url_handler(project=None, publishedName=None):
    try:
        image_url = json.loads(request.get_data().decode('utf-8'))['url']
        results = predict_url(image_url)
        return jsonify(results)
    except Exception as e:
        print('EXCEPTION:', str(e))
        return 'Error processing image'



if __name__ == '__main__':
    logging.config.fileConfig('./logging.conf')
    logger = logging.getLogger()
    print(f"Setting Logging level to {env.LOGGING_LEVEL} for all loggers")
    for handler in logger.handlers:
        handler.setLevel(env.LOGGING_LEVEL)
        handler.setFormatter(JSONFormatter())

    logger.info("Loading Model...")
    # Load and intialize the model
    initialize()
    logger.info("Model loaded and initialized...")

    env.start_metrics()


    logger.info("{} starting prediction endpoint at 0.0.0.0:{}".format(env.app_name,env.port))
    # Run the server
    app.run(host='0.0.0.0', port=env.port)
