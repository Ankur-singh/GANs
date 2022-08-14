from torch import nn

class Generator(nn.Module):
    def __init__(self, input_dim, output_dim) -> None:
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.LeakyReLU(0.01),
            nn.Linear(256, output_dim),
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x)


class Discriminator(nn.Module):
    def __init__(self, input_dim) -> None:
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.LeakyReLU(0.01),
            nn.Linear(256, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)


if __name__ == "__main__":
    import torch

    gen = Generator(16, 28*28)
    dis = Discriminator(28*28)

    z = torch.randn(3, 16)
    gen_z = gen(z)
    print(gen_z.shape)

    dis_z = dis(gen_z)
    print(dis_z.shape)