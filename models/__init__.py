#!/usr/bin/python3
"""
__init__ module
"""
import json
import uuid
import datetime
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
