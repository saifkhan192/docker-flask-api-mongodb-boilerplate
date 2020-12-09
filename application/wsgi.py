from app import app as application
import sys
import os
root_dir = os.path.dirname(__file__)
sys.path.append(root_dir)

# import logging
# from logging.handlers import RotatingFileHandler
# file_handler = RotatingFileHandler(root_dir+'/python.log', maxBytes=1024 * 1024 * 100, backupCount=20)
# file_handler.setLevel(logging.ERROR)
# formatter = logging.Formatter("\n\n  %(asctime)s - %(name)s - %(levelname)s - %(message)s ")
# file_handler.setFormatter(formatter)
# application.logger.addHandler(file_handler)
