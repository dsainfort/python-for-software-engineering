import pytest
from app.services import FullUserProfile

def valid_user_delete_id() -> int:
  	return 0

@pytest.fixture(scope="session")
def valid_user_delete_id() -> int:
  	return 0

@pytest.fixture(scope="session")
def sample_full_user_profile() -> FullUserProfile:
    return FullUserProfile(short_description="Short description",
						 long_bio="def",
						 username="abc",
						 liked_posts=[1, 2, 3])