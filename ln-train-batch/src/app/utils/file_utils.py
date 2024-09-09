import os

def ensure_directory_exists(path):
    """
    Ensure the directory exists; if not, create it.
    """
    if not os.path.exists(path):
        os.makedirs(path)
