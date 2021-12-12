import torch
from torch.utils.data import Dataset

from train import As
from train import Bs
from train import Cs


class LettersDataset(Dataset):

    def __init__(self):
        features = [*As, *Bs, *Cs]
        labels = [*[0 for _ in range(len(As))], *[1 for _ in range(len(Bs))], *[2 for _ in range(len(Cs))]]
        self.x = torch.tensor(features, dtype=torch.float32)
        self.y = torch.tensor(labels)
        self.n_samples = len(labels)

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return self.n_samples
