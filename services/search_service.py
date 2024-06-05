from models.bi_encoder import bi_encoder
from models.cross_encoder import cross_encoder
from utils.encoder import encode_single_text
from .db_service import get_all_posts, get_post_by_id

import torch
from sentence_transformers import util

def perform_search(query, top_k):
    posts = get_all_posts()
    embedded_query = bi_encoder.encode(query, convert_to_tensor=True)
    ids = [record['_id'] for record in posts]
    corpora = [record['corps'] for record in posts]
    embeddings = [torch.tensor(i['embedding']) for i in posts]
    hits = util.semantic_search(embedded_query, embeddings, top_k=top_k)
    hits = hits[0]
    cross_input = [[query, corpora[hit['corpus_id']]] for hit in hits]
    cross_scores = cross_encoder.predict(cross_input)

    result = sorted(zip(cross_scores, hits), key=lambda x: x[0], reverse=True)
    result_ids = [ids[hit['corpus_id']] for _, hit in result[:top_k]]
    
    return result_ids

def recommend_posts(post_id, top_k):
    post = get_post_by_id(post_id)
    if not post:
        return []

    query_text = post['corps']
    return perform_search(query_text, top_k)