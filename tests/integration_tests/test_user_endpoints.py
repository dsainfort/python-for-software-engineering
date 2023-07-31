
def test_delete_user_success(testing_app, valid_user_delete_id):
  response = testing_app.delete(f"/user/{valid_user_delete_id}")
  assert response.status_code == 200

def test_double_delete_user_fails(testing_app, valid_user_delete_id):
  response = testing_app.delete(f"/user/{valid_user_delete_id}")
  assert response.status_code == 200

  second_response = testing_app.delete(f"/user/{valid_user_delete_id}")
  assert second_response.status_code == 404
  assert response.json() == "User does not exist"

def test_delete_invalid_user_id_fails(testing_app, invalid_user_delete_id):
  response = testing_app.delete(f"/user/{invalid_user_delete_id}")
  assert response.status_code == 404
  assert response.json() == "User does not exist"

def test_put_user_returns_correct_results(testing_app, sample_full_user_profile):
  user_id = 1
  response = testing_app.put(f"/user/{user_id}", json=sample_full_user_profile.dict())

  assert response.status_code == 200