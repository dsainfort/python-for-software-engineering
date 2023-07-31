import pytest
from app.services.user import UserService


@pytest.fixture
def _profile_infos():
	return {
		0: {
			"short_description": "Bio description",
			"long_bio": "More detailed information"
		}
	}


@pytest.fixture
def _users_content():
	return {
		0: {
			"liked_posts": [1] * 9,
		}
	}


@pytest.fixture
def user_service(profile_infos, users_content):
	return UserService(profile_infos, users_content)


@pytest.fixture(scope="function")
def testing_fixture():
    print("Initializing fixture")
    return 'a'
