import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from .. import constants
from ..model import NeuralNet
from dataset import LettersDataset

if __name__ == '__main__':

    dataset = LettersDataset()
    train_loader = DataLoader(dataset=dataset, batch_size=5, shuffle=True)

    model = NeuralNet(constants.input_size, constants.hidden_size, constants.num_classes)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=constants.learning_rate)

    n_total_steps = 2
    for epoch in range(constants.num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            images = images.reshape(-1, 5 * 7)
            outputs = model(images)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i + 1) % 100 == 0:
                print(f'Epoch [{epoch + 1}/{constants.num_epochs}], Step [{i + 1}/{n_total_steps}], Loss: {loss.item():.4f}')

    torch.save(model.state_dict(), constants.PATH)
