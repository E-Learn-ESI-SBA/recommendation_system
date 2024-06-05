from models.bi_encoder import bi_encoder

def encode_single_text(text):
    return bi_encoder.encode(text, convert_to_tensor=True)