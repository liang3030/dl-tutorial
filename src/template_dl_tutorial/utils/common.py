import os
from box.exceptions import BoxValueError
import yaml
from template_dl_tutorial import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (Path): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
	
@ensure_annotations
def create_directories(path_to_dir: list, verbose=True):
	"""create list of directories

	Args:
		path_to_dir (list): list of directories
		ignore_log (bool, optional): ignore if multiple dirs is to be created.
	"""
	for path in path_to_dir:
		os.makedirs(path, exist_ok=True)
		if verbose:
			logger.info(f"Created directory at {path}")

@ensure_annotations
def save_json(path: Path, data:dict):
	"""save json file

	Args:
		path (Path): path to save
		data (dict): data to be saved in json file
	"""
	with open(path, 'w') as f:
		json.dump(data, f, indent=2)

	logger.info(f"Saved json file at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
	"""load json file

	Args:
		path (Path): path to load

	Returns:
		ConfigBox: data as class attributes instead of dict
	"""
	with open(path) as f:
		content = json.load(f)

	logger.info(f"Loaded json file from {path}")
	return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
	"""save binary file

	Args:
		data (Any): data to be saved
		path (Path): path to save
	"""
	joblib.dump(value=data, filename=path)
	logger.info(f"Saved binary file at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
	"""load binary file

	Args:
		path (Path): path to load

	Returns:
		Any: loaded data
	"""
	data = joblib.load(path)
	logger.info(f"Loaded binary file from {path}")
	return data

@ensure_annotations
def get_size(path: Path) -> str:
	"""get size of file in KB

	Args:
		path (Path): path to file

	Returns:
		str: size of KB
	"""
	size = round(os.path.getsize(path) / 1024)
	logger.info(f"Size of file at {path} is {size}")
	return f"~ {size} KB"

def decodeImage(imgstring, fileName):
	imgdata = base64.b64decode(imgstring)
	with open(fileName, 'wb') as f:
		f.write(imgdata)
		f.close()

def encodeImageIntoBase64(croppedImagePath):
	with open(croppedImagePath, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
		return encoded_string.decode('utf-8')
