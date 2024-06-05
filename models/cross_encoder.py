from sentence_transformers import CrossEncoder

cross_encoder = CrossEncoder("./tools/cross_encoder", device='cpu')