import os
import tempfile

import pytest

import app


# @pytest.fixture
# def client():
#     db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
#     app.app.config['TESTING'] = True

#     with app.app.test_client() as client:
#         with app.app.app_context():
#             app.app.init_db()
#         yield client

#     os.close(db_fd)
#     os.unlink(app.app.config['DATABASE'])
@pytest.fixture
def api():
    
    api = app.app.test_client()
    return api
