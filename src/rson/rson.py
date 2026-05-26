from os import PathLike
from .get_bin import __get_bin_path__
from .error import RSONError
import json
import subprocess

RSON_PATH = __get_bin_path__()


def loadf(path: PathLike, display_classes: bool = False):
    try:
        result = subprocess.run([RSON_PATH, "lower", "--file", path, 
                    "--display-classes", str(display_classes), "--keep-ast", "false"], capture_output=True, check=True)

        return json.loads(result.stdout)

    except subprocess.CalledProcessError as e:
        raise RSONError(f"An error occurred while trying to load the file at '{path}': {e.stderr}")
    

def loads(string: str, display_classes: bool = False):
    try:
        result = subprocess.run([RSON_PATH, "lower", "--input", string, 
                    "--display-classes", str(display_classes), "--keep-ast", "false"], capture_output=True, check=True)

        return json.loads(result.stdout)

    except subprocess.CalledProcessError as e:
        raise RSONError(f"An error occurred while trying to load the input: {e.stderr}")
