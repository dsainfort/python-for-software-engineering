from fastapi.testclient import TestClient
import pytest
from main import create_application

@pytest.fixture(scope="session")
def testing_app():
  app = create_application()
  return TestClient(app)
