
from flask import Flask, render_template


HOST = "localhost"
PORT = 8000


def create_app():
    """
    Create the analytical flask application
            # app.add_url_rule("/", endpoint="index")
    :return:
    """
    app = Flask(__name__, template_folder='./templates', static_folder="assets")

    @app.route("/")
    def home():
        return render_template("home.html")

    return app


def run_app(app, host=HOST, port=PORT):
    """
    Run the analytical flask application
    :param app:
    :param host:
    :param port:
    :return:
    """
    app.run(host=host, port=port)


if __name__ == "__main__":
    run_app(create_app())

