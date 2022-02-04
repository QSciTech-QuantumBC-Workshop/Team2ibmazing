import numpy as np
import torch

class AE(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
        # Linear encoder composed of linear layers alternating with sigmoidal activation functions
        # Compress input from sixty features to five features
        self.encoder = torch.nn.Sequential(
            torch.nn.Linear(60, 52),
            torch.nn.ReLU(),
            torch.nn.Linear(52, 44),
            torch.nn.ReLU(),
            torch.nn.Linear(44, 32),
            torch.nn.ReLU(),
            torch.nn.Linear(32, 24),
            torch.nn.ReLU(),
            torch.nn.Linear(24, 16),
            torch.nn.ReLU(),
            torch.nn.Linear(16, 5)
        )
        
        # Linear decoder that maps five features back to sixty
        self.decoder = torch.nn.Sequential(
            torch.nn.Linear(5, 16),
            torch.nn.ReLU(),
            torch.nn.Linear(16, 24),
            torch.nn.ReLU(),
            torch.nn.Linear(24, 32),
            torch.nn.ReLU(),
            torch.nn.Linear(32, 44),
            torch.nn.ReLU(),
            torch.nn.Linear(44, 52),
            torch.nn.ReLU(),
            torch.nn.Linear(52, 60),
            torch.nn.Sigmoid()
        )
        
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded