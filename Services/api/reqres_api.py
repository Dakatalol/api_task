import requests
from Utils.api_utility import ApiInteractions

"""
6. Parametrize base URL
"""


class ReqresApi:
    """
    This class allows the user to hit the various endpoints that are accessible in the reqres service
    and returns the response back to be used to validate the responses.
    """
    base_url = f'https://reqres.in/api/'
    auth = None
    headers = {'Content-Type': 'application/json'}

    # GET Requests
    @classmethod
    def get_list_of_users_per_page(cls, page_number):
        return ApiInteractions.get(cls.base_url + 'users/?page=' + str(page_number),
                                   header_data=cls.headers)

    @classmethod
    def get_user_by_id(cls, user_id):
        return ApiInteractions.get(cls.base_url + 'users/' + str(user_id),
                                   header_data=cls.headers)

    # POST Requests
    @classmethod
    def create_user(cls, json):
        return ApiInteractions.post(cls.base_url + 'users/',
                                    header_data=cls.headers,
                                    json=json)

    # DELETE Requests
    @classmethod
    def delete_user(cls, user_id):
        return ApiInteractions.delete(cls.base_url + 'users/' + user_id,
                                      header_data=cls.headers)

