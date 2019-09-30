import pytest
from config import TestingConfig, Config
from app import app, db


def test_test_conf():
    app.config.from_object(TestingConfig)
    assert app.config['DEBUG']
    assert app.config['SQLALCHEMY_DATABASE_URI']
    assert app.config['TESTING']


def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello World!' in response.data

def test_db():


        from models import Articles

        t_book = Articles(
            name='aaaa',
            author='aaaaa',
            published= 2001
        )
        db.session.add(t_book)
        db.session.commit()

        #assert db.session.query(Articles).one()