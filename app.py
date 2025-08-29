from flask import Flask
from flask_cors import CORS
from routes import auth_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/')

    # Apply CORS here with frontend domain whitelisted
    CORS(app, resources={
        r"/*": {"origins": "https://attendify-frontend-560n.onrender.com"}
    })

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
