#!/usr/bin/python3
"""models package
defines class models for app
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
