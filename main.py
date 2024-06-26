#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
import router

def create_app():
    # Generate Flask App Instance
    app = Flask(__name__)

    # Register Router Instance
    app.register_blueprint(router.router)

    # Additional Configuration 
    app.config['JSON_AS_ASCII'] = False #日本語文字化け対策
    app.config["JSON_SORT_KEYS"] = False #ソートをそのまま
    CORS(
        app,
        resources = {
            r"/api/*": {"origins": ["http://localhost", "http://localhost:4200"]}
        }
    )
    return app

app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080, threaded=True, use_reloader=False)
