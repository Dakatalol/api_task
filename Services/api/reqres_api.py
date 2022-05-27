import requests


class ReqresApi:
    """
    This class allows the user to hit the various endpoints that are accessible in the reqres service
    and returns the response back to be used to validate the responses.
    """
    base_url = f'https://reqres.in/api/'
    auth = None
    headers = {'Content-Type': 'application/json'}
    params = {}

    # GET Requests
    @classmethod
    def get_list_of_users_per_page(cls, page_number):
        return requests.get(cls.base_url + 'users/?page=' + str(page_number), headers=cls.headers)

    @classmethod
    def get_user_by_id(cls, user_id):
        return requests.get(cls.base_url + 'users/' + str(user_id), headers=cls.headers)

    # POST Requests
    @classmethod
    def create_user(cls, json):
        return requests.post(cls.base_url + 'users/', headers=cls.headers, json=json)

    # DELETE Requests
    @classmethod
    def delete_user(cls, user_id):
        return requests.delete(cls.base_url + 'users/' + user_id, headers=cls.headers)
