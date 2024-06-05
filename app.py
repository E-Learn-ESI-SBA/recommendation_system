from flask import Flask
from routes.search import search_bp
from routes.recommend import recommend_bp
from routes.encode import encode_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(search_bp)
    app.register_blueprint(recommend_bp)
    app.register_blueprint(encode_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)