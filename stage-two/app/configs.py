"""
    Configuration Manager
"""
import os

BASE_URL =  os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMT_DATABASE_URI = os.path.join(BASE_URL, "db.sqlite")
    