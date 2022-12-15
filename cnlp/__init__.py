import logging


logger_format = "\033[36m[%(asctime)s %(msecs)03dms %(threadName)s]\033[0m %(message)s";
logging.basicConfig(format=logger_format, level=logging.INFO, datefmt="%I:%M:%S");
LOG = logging.info;

# Initialize the global setting
GSET = {};

GSET['LANGUAGE_PROCESSED']      = 'FR';     # Set the langauge processed on 'French' by default.
GSET['WORKSPACE_DIR']           = './';     # Set the workspace directory on currente directory.


