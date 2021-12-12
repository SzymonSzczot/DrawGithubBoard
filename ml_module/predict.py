import torch

import constants
from utils import load_model


class Predictor:

    def __init__(self, model_path=constants.PATH):
        self.model = load_model(model_path)

    def predict(self, input_value):
        assert len(input_value) == 7
        assert len(input_value[0]) == 5
        with torch.no_grad():
            image = input_value.reshape(-1, 5 * 7)
            outputs = self.model(image)
            return torch.max(outputs.data, 1)
