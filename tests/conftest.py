import pytest
from flask import current_app

from app.main import *


@pytest.fixture(scope="function")
def client():
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"
        yield client
