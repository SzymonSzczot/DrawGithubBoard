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
            input_tensor = torch.tensor(input_value, dtype=torch.float32)
            image = input_tensor.reshape(-1, 5 * 7)
            outputs = self.model(image)
            v, p = torch.max(outputs.data, 1)
            return {
                "confidence": v.item(),
                "class": p.item()
            }
