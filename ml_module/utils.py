import torch

import constants
from model import NeuralNet


def load_model(model_path):
    loaded_model = NeuralNet(constants.input_size, constants.hidden_size, constants.num_classes)
    loaded_model.load_state_dict(torch.load(model_path))
    loaded_model.eval()
    return loaded_model
