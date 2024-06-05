from flask import Blueprint, request, jsonify
from services.search_service import perform_search

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['POST'])
def search_posts():
    data = request.get_json()
    query = data.get('query')
    top_k = data.get('top_k', 12)  # Default to 12 if top_k is not provided

    if not query:
        return jsonify({'error': 'Query is required'}), 400

    result_ids = perform_search(query, top_k)
    return jsonify({'ids': result_ids})