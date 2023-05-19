import os

from pathlib import Path


PROJ_DIR = Path(__file__).parent.absolute()

DATA_DIR = os.path.join(PROJ_DIR, "data")
PREFERENCES_DIR = os.path.join(DATA_DIR, "preferences")
EXAMPLES_DIR = os.path.join(DATA_DIR, "examples")






