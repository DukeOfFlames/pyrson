import sys
from pathlib import Path

def __get_bin_path__() -> Path:
    # Navigate to module root.
    here = Path(__file__).parent.parent.parent

    # Choose file based on OS.
    if sys.platform == "win32":
        return here / "binaries" / "windows" / "rson.exe"
    elif sys.platform in ["darwin", "linux"]:
        return here / "binaries" / "linux" / "rson"
    else: raise Exception(f"{sys.platform} is not supported yet.")
