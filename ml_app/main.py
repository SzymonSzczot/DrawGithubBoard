import json

from flask import Flask
from flask import request

from train.data import desired_results
from predict import Predictor

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    image = json.loads(request.data)
    predictor = Predictor()
    prediction = predictor.predict(image["matrix"])
    desired_result = desired_results[prediction["class"]]
    return {
        **prediction,
        "model_result": desired_result
    }


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
