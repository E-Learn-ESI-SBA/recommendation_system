from sentence_transformers import SentenceTransformer

bi_encoder = SentenceTransformer("./tools/bi_encoder", device='cpu')
bi_encoder.max_seq_length = 340