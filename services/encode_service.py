# /services/encode_service.py

from pymongo import MongoClient
from utils.encoder import encode_single_text
from services.db_service import add_post

def encode_and_store_posts(id,post):
    encoded_vector = encode_single_text(post).cpu().numpy().tolist()
    add_post(id,post,encoded_vector)
    return post,encoded_vector