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
    with app.app_context() as context:
        context.push()
        db.drop_all()
        db.create_all()

        from models import Articles

        test_art = Articles(name="article article", author = "author article", published= "13.04.2001")
        test_art.save()
        db.session.commit()

    assert db.session.query(Articles).one()