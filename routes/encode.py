# /routes/encode.py

from flask import Blueprint, request, jsonify
from services.encode_service import encode_and_store_posts

encode_bp = Blueprint('encode_bp', __name__)

@encode_bp.route('/encode', methods=['POST'])
def encode():
    data = request.json
    posts = data.get('post',[])
    id = data.get("_id",[])
    if not posts:
        return jsonify({"error": "No posts provided"}), 400
    if not id:
        return jsonify({"error": "No id provided"}), 400
    encoded_data = encode_and_store_posts(id,posts)
    return jsonify({"encoded_data": encoded_data}), 200