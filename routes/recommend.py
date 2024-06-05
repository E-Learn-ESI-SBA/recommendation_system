from flask import Blueprint, request, jsonify
from services.search_service import recommend_posts

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    post_id = data.get('post_id')
    top_k = data.get('top_k', 12)  # Default to 12 if top_k is not provided

    if post_id is None:
        return jsonify({'error': 'Post ID is required'}), 400

    result_ids = recommend_posts(post_id, top_k)
    return jsonify({'ids': result_ids})