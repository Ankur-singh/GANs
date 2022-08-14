import config
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import Generator, Discriminator

## Data
tfms = transforms.Compose([
    transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))
])

train_ds = datasets.MNIST(root="data/", train=True, transform=tfms, download=True)
train_dl = DataLoader(train_ds, batch_size=config.BS, shuffle=True)

## Model, loss & optimizer
generator = Generator(config.Z_DIM, config.OUT_DIM)
discriminator = Discriminator(config.OUT_DIM)

loss = nn.BCELoss()

gen_opt = torch.optim.Adam(generator.parameters(), lr=config.LR)
dis_opt = torch.optim.Adam(discriminator.parameters(), lr=config.LR)

## Training
for xb, yb in train_dl:
    xb = xb.view(config.BS, -1)

    ## Generator
    zb = torch.randn(config.BS, config.Z_DIM)
    fake = generator(zb)

    
    ## discriminator
    dis_fake = discriminator(fake)
    dis_fake_loss = loss(dis_fake, torch.zeros_like(dis_fake))
    dis_real_loss = loss(xb, torch.ones_like(xb))
    dis_loss = (dis_fake_loss + dis_real_loss)/2

    