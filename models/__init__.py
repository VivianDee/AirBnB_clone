#!/usr/bin/python3
"""Acts as storage for the instance objects"""

import sys
import os
script_directory = os.path.dirname(os.path.abspath(__file__))
project_directory = os.path.abspath(os.path.join(script_directory, '..'))
sys.path.append(project_directory)
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
