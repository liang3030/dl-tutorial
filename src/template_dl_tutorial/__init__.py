# A logging function is defined in the utils/__init__.py file. The logging function is used in the template.py file to log messages. The setup.py file imports the logging function from the utils/__init__.py file to log messages during the setup process. The logging function is used to log messages during the setup process.
import os
import sys
import logging

logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"

log_dir = "logs"

log_filepath = os.path.join(log_dir, 'running_logs.log')

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
	level=logging.INFO, 
	format=logging_str, 
	handlers=[
		logging.FileHandler(log_filepath),
		logging.StreamHandler(sys.stdout)
	]
)

logger = logging.getLogger('dl-tutorial')