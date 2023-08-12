#!/usr/bin/python3
"""Acts as storage for the instance objects"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
