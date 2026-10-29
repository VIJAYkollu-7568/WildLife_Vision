import torch
import torch.nn as nn

# -------------------------
# Simple Generator
# -------------------------
class SimpleGenerator(nn.Module):
    def __init__(self, input_nc=3, output_nc=3):
        super(SimpleGenerator, self).__init__()

        # Encoder (downsample)
        self.down = nn.Sequential(
            nn.Conv2d(input_nc, 64, kernel_size=4, stride=2, padding=1),  # (B, 3, 128, 128) -> (B, 64, 64, 64)
            nn.ReLU(True),
            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),       # (B, 64, 64, 64) -> (B, 128, 32, 32)
            nn.ReLU(True)
        )

        # Bottleneck
        self.middle = nn.Sequential(
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.ReLU(True)
        )

        # Decoder (upsample)
        self.up = nn.Sequential(
            nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),  # (B, 128, 32, 32) -> (B, 64, 64, 64)
            nn.ReLU(True),
            nn.ConvTranspose2d(64, output_nc, kernel_size=4, stride=2, padding=1),  # -> (B, 3, 128, 128)
            nn.Tanh()  # Output between -1 and 1
        )

    def forward(self, x):
        x = self.down(x)
        x = self.middle(x)
        x = self.up(x)
        return x


# -------------------------
# Simple Discriminator
# -------------------------
class SimpleDiscriminator(nn.Module):
    def __init__(self, input_nc=3):
        super(SimpleDiscriminator, self).__init__()

        self.model = nn.Sequential(
            nn.Conv2d(input_nc, 64, kernel_size=4, stride=2, padding=1),  # (B, 3, 128, 128) -> (B, 64, 64, 64)
            nn.LeakyReLU(0.2, True),

            nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),      # (B, 64, 64, 64) -> (B, 128, 32, 32)
            nn.LeakyReLU(0.2, True),

            nn.Conv2d(128, 1, kernel_size=4, stride=2, padding=1),       # (B, 128, 32, 32) -> (B, 1, 16, 16)
            nn.Sigmoid()  # Probability of real/fake
        )

    def forward(self, x):
        return self.model(x)


# -------------------------
# Test the models
# -------------------------
if __name__ == "__main__":
    gen = SimpleGenerator()
    disc = SimpleDiscriminator()

    # Dummy input (batch_size=1, channels=3, image=128x128)
    img = torch.randn(1, 3, 128, 128)

    fake_img = gen(img)
    disc_output = disc(fake_img)

