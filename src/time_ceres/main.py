import sys

from time_ceres.settings import PROJ_DIR
from time_ceres.server.app import create_app, run_app


sys.path.insert(0, PROJ_DIR)


if __name__ == "__main__":
    run_app(create_app())
