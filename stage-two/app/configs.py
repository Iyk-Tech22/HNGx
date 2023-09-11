"""
    Configuration Manager
"""
import os

BASE_URL =  os.path.abspath(os.path.dirname(__file__))

class Config():
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_URL, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "amacodeguru"
