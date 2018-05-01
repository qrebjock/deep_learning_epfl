import torch.nn as nn
from torch.nn import functional as F

from nnmodel import NNModel


class Net(NNModel):

    """def __init__(self):
        super(Net, self).__init__()
        nb_hidden = 32
        self.conv1 = nn.Conv1d(28, 32, kernel_size=5, padding=2)
        # self.batch_nom1= nn.BatchNorm1d(32)
        self.conv2 = nn.Conv1d(32, 32, kernel_size=3, padding=1)
        self.batch_nom2 = nn.BatchNorm1d(32)
        self.conv3 = nn.Conv1d(32, 32, kernel_size=3, padding=1)
        self.conv3_drop = nn.Dropout()
        self.batch_nom3 = nn.BatchNorm1d(32)
        self.fc1 = nn.Linear(12 * 32, nb_hidden)
        self.fc2 = nn.Linear(nb_hidden, 2)

    def forward(self, x):
        x = F.relu(F.max_pool1d(self.conv1(x), kernel_size=2))
        x = F.relu(self.batch_nom2(F.max_pool1d(self.conv2(x), kernel_size=2)))
        x = F.relu(self.batch_nom3(self.conv3_drop(self.conv3(x))))
        x = F.relu(self.fc1(x.view(-1, 12*32)))
        # x = F.dropout(x,training=self.training)
        x = self.fc2(x)
        return x"""

    def __init__(self):
        super(Net, self).__init__()
        nb_hidden = 32
        self.conv1 = nn.Conv1d(1, 32, kernel_size=5, padding=2)
        # self.batch_nom1= nn.BatchNorm1d(32)
        self.conv2 = nn.Conv1d(32, 32, kernel_size=3, padding=1)
        self.batch_nom2 = nn.BatchNorm1d(32)
        self.conv3 = nn.Conv1d(32, 32, kernel_size=3, padding=1)
        self.conv3_drop = nn.Dropout()
        self.batch_nom3 = nn.BatchNorm1d(32)
        self.fc1 = nn.Linear(350 * 32, nb_hidden)
        self.fc2 = nn.Linear(nb_hidden, 2)

    def forward(self, x):
        x = F.relu(F.max_pool1d(self.conv1(x), kernel_size=2))
        x = F.relu(self.batch_nom2(F.max_pool1d(self.conv2(x), kernel_size=2)))
        x = F.relu(self.batch_nom3(self.conv3_drop(self.conv3(x))))
        x = F.relu(self.fc1(x.view(-1, 350 * 32)))
        # x = F.dropout(x,training=self.training)
        x = self.fc2(x)
        return x


class TestNet(NNModel):

    def __init__(self):
        super(TestNet, self).__init__()
        nb_hidden = 32
        self.conv1 = nn.Conv1d(1, 32, kernel_size=5, padding=2)
        # self.batch_nom1= nn.BatchNorm1d(32)
        self.conv2 = nn.Conv1d(32, 32, kernel_size=3, padding=1)
        self.batch_nom2 = nn.BatchNorm1d(32)
        self.conv3 = nn.Conv1d(32, 32, kernel_size=3, padding=1)
        self.conv3_drop = nn.Dropout()
        self.batch_nom3 = nn.BatchNorm1d(32)
        self.fc1 = nn.Linear(12 * 32, nb_hidden)
        self.fc2 = nn.Linear(nb_hidden, 2)

    def forward(self, x):
        x = F.relu(F.max_pool1d(self.conv1(x), kernel_size=2))
        x = F.relu(self.batch_nom2(F.max_pool1d(self.conv2(x), kernel_size=2)))
        x = F.relu(self.batch_nom3(self.conv3_drop(self.conv3(x))))
        x = F.relu(self.fc1(x.view(-1, 175 * 32)))
        # x = F.dropout(x,training=self.training)
        x = self.fc2(x)
        return x