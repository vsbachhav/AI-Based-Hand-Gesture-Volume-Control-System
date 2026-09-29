from flask import Flask
from flask_cors import CORS

from api.routes import api

from config import UPLOAD_FOLDER, MAX_CONTENT_LENGTH


def create_app():

    app = Flask(__name__)

    CORS(app)

    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

    app.register_blueprint(
        api,
        url_prefix="/api"
    )

    return app


app = create_app()


if __name__ == "__main__":

    print("=" * 60)
    print("AI DOCUMENT INTELLIGENCE BACKEND")
    print("=" * 60)
    print("Server: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )