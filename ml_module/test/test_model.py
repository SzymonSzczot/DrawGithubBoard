import torch
from torch.utils.data import DataLoader
from torch.utils.data import Dataset

import constants
from utils import load_model


class LettersDatasetTest(Dataset):
    def __init__(self):
        test = [
            [
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
            ],
            [
                [1, 1, 1, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0],
            ],
            [
                [1, 1, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 0, 0],
            ],
            [
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
            ]
        ]
        self.x = torch.tensor(test, dtype=torch.float32)
        labels = [0, 1, 1, 2]
        self.y = torch.tensor(labels)
        self.n_samples = len(labels)

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return self.n_samples


if __name__ == '__main__':

    test_dataset = LettersDatasetTest()
    test_loader = DataLoader(dataset=test_dataset)

    loaded_model = load_model(constants.PATH)

    with torch.no_grad():
        n_correct = 0
        n_samples = 0
        for images, labels in test_loader:
            images = images.reshape(-1, 5 * 7)
            print(images)
            outputs = loaded_model(images)
            # max returns (value ,index)
            _, predicted = torch.max(outputs.data, 1)
            print(predicted)
            n_samples += labels.size(0)
            n_correct += (predicted == labels).sum().item()

        acc = 100.0 * n_correct / n_samples
        print(f'Accuracy of the network on the test images: {acc} %')
