import pytest

from Services.api.reqres_api import ReqresApi
from Data.Users.list_users import LIST_OF_USERS_ON_PAGE_1
from Data.Users.single_user import user_id_2, invalid_user
from Data.Users.new_user import RANDOM_NEW_USER
from utils.Utils import Utils

pytestmark = [pytest.mark.regression, pytest.mark.smome]


@pytest.mark.smoke
def test_verify_user_list_is_returned_correct():
    """
    GET /api/user?page=1
    Execute one or many JSON response Assertions
    """
    response = ReqresApi.get_list_of_users_per_page(LIST_OF_USERS_ON_PAGE_1['INPUT_REQUEST_BODY'])
    result = response.json()

    assert result == LIST_OF_USERS_ON_PAGE_1['EXPECTED_RESPONSE_BODY']


@pytest.mark.smoke
def test_verify_extracted_single_user_details_is_returned_correct():
    """
    Extract single user details(ID, Email)
    """
    response = ReqresApi.get_list_of_users_per_page(LIST_OF_USERS_ON_PAGE_1['INPUT_REQUEST_BODY'])
    result = response.json()
    extracted_user_id_and_email = {result['data'][0]['id']: result['data'][0]['email']}

    assert {1: 'george.bluth@reqres.in'} == extracted_user_id_and_email


@pytest.mark.regression
def test_extract_users_and_sort_by_first_name():
    """
    (Optional) Extract all users, sort them by First Name alphabetically. Print sorted collection.
    """
    response = ReqresApi.get_list_of_users_per_page(LIST_OF_USERS_ON_PAGE_1['INPUT_REQUEST_BODY'])
    result = response.json()
    extracted_users = result['data']

    sorted_users = Utils.sort_user_by_first_name(extracted_users)
    print(sorted_users)


@pytest.mark.smoke
def test_extract_user_by_id_and_verify_response():
    """
    GET /api/users/{USER_ID}
    Execute one or many JSON Response Assertions
    """
    response = ReqresApi.get_user_by_id(user_id_2['INPUT_REQUEST_BODY'])
    result = response.json()

    assert result == user_id_2['EXPECTED_RESPONSE_BODY']


@pytest.mark.smoke
def test_extract_invalid_user_by_id_and_verify_response():
    """
    GET /api/users/{USER_ID}
    Execute one or many assertions
    """
    response = ReqresApi.get_user_by_id(invalid_user['INPUT_REQUEST_BODY'])
    result = response.json()

    assert response.status_code == 404
    assert result == invalid_user['EXPECTED_RESPONSE_BODY']


@pytest.mark.smoke
def test_create_unique_user():
    """
    POST /api/users
    Execute one or many JSON Response Assertions
    """
    response = ReqresApi.create_user(RANDOM_NEW_USER['INPUT_REQUEST_BODY'])
    print("Created: " + response.text)
    assert response.status_code == 201


@pytest.mark.smoke
def test_create_and_delete_unique_user():
    """
    POST /api/users
    Execute one or many JSON Response Assertions
    """

    # creating the user
    response = ReqresApi.create_user(RANDOM_NEW_USER['INPUT_REQUEST_BODY'])
    # getting users id
    user_id = response.json()['id']
    print("Created: " + response.text)

    # deleting the user by id
    delete_response = ReqresApi.delete_user(user_id)
    assert delete_response.status_code == 204

    # verifying user is not existing
    deleted_user_response = ReqresApi.get_user_by_id(user_id)
    assert deleted_user_response.status_code == 404
