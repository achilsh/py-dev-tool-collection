import pytest
from app.main import app
from app.core.log import logger
from fastapi.testclient import TestClient
    # 确保测试用户存在
from app.models.user import UserModel
from tortoise.contrib.test import TestCase


### pytest ./tests/test_user.py

@pytest.fixture
def test_client():
    return TestClient(app)

def test_get_user_info(test_client): 
    user = UserModel.create(
        name="test_user",
        email="test@example.com",
        cardId="test_card_123",
        address="Test Address"
    )

    input_data = {
        "id":100,
        "username":"demo_user",
        "email":"hwshtongxin@126.com"
    }
    response = test_client.post("http://127.0.0.1:8080/demo/v1/user/call/get_info", json=input_data)
    assert response.status_code == 200 
    resp_json = response.json()
    logger.info(f"response: {resp_json}")

