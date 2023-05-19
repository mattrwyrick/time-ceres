import sys

from flask import Flask

from time_ceres.settings import PROJ_DIR


sys.path.insert(0, PROJ_DIR)

HOST = "localhost"
PORT = 8000


def create_app():
    """
    Create the analytical flask application
            # app.add_url_rule("/", endpoint="index")
    :return:
    """
    app = Flask(__name__)

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app


if __name__ == "__main__":
    create_app().run(host=HOST, port=PORT)

