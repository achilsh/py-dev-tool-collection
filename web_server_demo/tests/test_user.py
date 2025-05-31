import pytest
from app.main import app
from app.core.log import logger
from fastapi.testclient import TestClient


### pytest ./tests/test_user.py

@pytest.fixture
def test_client():
    return TestClient(app)

def test_get_user_info(test_client): 
    input_data = {
        "id":100,
        "username":"demo_user",
        "email":"hwshtongxin@126.com"
    }
    response = test_client.post("http://127.0.0.1:8080/demo/v1/user/call/get_info", json=input_data)
    assert response.status_code == 200 
    resp_json = response.json()
    logger.info(f"response: {resp_json}")

