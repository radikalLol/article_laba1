import pytest
from config import TestingConfig, Config
from app import app, db


def test_test_conf():
    app.config.from_object(TestingConfig)
    assert app.config['DEBUG']
    assert app.config['SQLALCHEMY_DATABASE_URI']
    assert app.config['TESTING']