# embeddings/model.py
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class TwoTowerModel(nn.Module):
    def __init__(self, text_dim=768, sku_dim=256, hidden_dim=512, emb_dim=128):
        super().__init__()
        self.query_tower = nn.Sequential(
            nn.Linear(text_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, emb_dim)
        )
        self.sku_tower = nn.Sequential(
            nn.Linear(sku_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, emb_dim)
        )

    def forward(self, query_vec, sku_vec):
        q = F.normalize(self.query_tower(query_vec), p=2, dim=-1)
        s = F.normalize(self.sku_tower(sku_vec), p=2, dim=-1)
        return q, s

def cosine_similarity_loss(q, s):
    sim = (q * s).sum(dim=-1)
    return 1 - sim.mean()

_model = TwoTowerModel()
_model.eval()

def encode_query(text: str):
    # placeholder: in real system, plug in text encoder
    with torch.no_grad():
        dummy_query = torch.randn(1, 768)
        dummy_sku = torch.randn(1, 256)
        q, _ = _model(dummy_query, dummy_sku)
        return q[0].cpu().numpy().astype(np.float32)
