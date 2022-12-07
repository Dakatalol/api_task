import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1


class ApiInteractions:
    """
    Helper utility for making CRUD operations on end points. Works with no auth, OAuth1 and Basic Auth.

    Example:
        Default authorization is no auth. Use 'oauth1' or 'basic' in conjunction with 'auth_data' to override.
        'auth_data' requires the following values for each authorization type:

        Request with OAuth1 authorization:
        authorization='oauth1'
        auth_data={ 'application_key': 'value', 'application_secret': 'value' }

        Request with Basic authorization:
        authorization='basic'
        auth_data={ 'username': 'value', 'password': 'value' }

    Example:
        To access response data, you can use the following:

        response.status_code - Response staus code

        response.url - Response URL

        response.text - Response body
    """
    AUTH_OPTIONS = {'oauth1', 'basic', None}

    @classmethod
    def get(cls, url: str, authorization: str = None, header_data: dict = None, auth_data: dict = None,
            allow_redirects: bool = True):
        """
        Perform a GET request

        Args:
            url: Endpoint URL
            authorization: Authorization type.
                Options: 'oauth1', 'basic', None
            header_data: JSON formatted Headers for the request
            auth_data: Authorization data to be formatted
            allow_redirects: Override if you want to prevent any redirects from occurring

        Returns:
            Response data from the request
        """
        auth = cls.__get_authorization(authorization=authorization, auth_data=auth_data)
        return requests.get(url, auth=auth, headers=header_data, allow_redirects=allow_redirects)

    @classmethod
    def delete(cls, url: str, authorization: str = None, header_data: dict = None, auth_data: dict = None,
               allow_redirects: bool = True):
        """
        Perform a DELETE request

        Args:
            url: Endpoint URL
            authorization: Authorization type.
                Options: 'oauth1', 'basic', None
            header_data: JSON formatted Headers for the request
            auth_data: Authorization data to be formatted
            allow_redirects: Override if you want to prevent any redirects from occurring

        Returns:
            Response data from the request
        """
        auth = cls.__get_authorization(authorization=authorization, auth_data=auth_data)
        return requests.delete(url, auth=auth, headers=header_data, allow_redirects=allow_redirects)

    @classmethod
    def post(cls, url: str, json: any, authorization: str = None, header_data: dict = None, files=None,
             auth_data: dict = None, allow_redirects: bool = True):
        """
        Perform a POST request

        Args:
            url: Endpoint URL
            json: Body of the request in json format
            authorization: Authorization type.
                Options: 'oauth1', 'basic', None
            header_data: JSON formatted Headers for the request
            files: file object(s) to send with request
            auth_data: Authorization data to be formatted
            allow_redirects: Override if you want to prevent any redirects from occurring

        Returns:
            Response data from the request
        """
        auth = cls.__get_authorization(authorization=authorization, auth_data=auth_data)
        return requests.post(url, json=json, auth=auth, headers=header_data, files=files,
                             allow_redirects=allow_redirects)

    @classmethod
    def put(cls, url: str, authorization: str = None, json=None, header_data: dict = None, files=None,
            auth_data: dict = None, allow_redirects: bool = True):
        """
        Perform a PUT request

        Args:
            url: Endpoint URL
            authorization: Authorization type.
                Options: 'oauth1', 'basic', None
            json: Body of the request in json format
            header_data: JSON formatted Headers for the request
            files: file object(s) to send with request
            auth_data: Authorization data to be formatted
            allow_redirects: Override if you want to prevent any redirects from occurring

        Returns:
            Response data from the request
        """
        auth = cls.__get_authorization(authorization=authorization, auth_data=auth_data)
        return requests.put(url, json=json, auth=auth, headers=header_data, files=files,
                            allow_redirects=allow_redirects)

    @classmethod
    def __get_authorization(cls, authorization: str, auth_data: dict = None):
        """
        Helper method to format the authorization of a request

        Args:
            authorization: Authorization type.
                Options: 'oauth1', 'basic', None
            auth_data: Authorization data to be formatted

        Raises:
            ValueError: If authorization is not 'oauth1', 'basic' or None

        Returns:
            Formatted authorization data or None
        """
        if authorization not in cls.AUTH_OPTIONS:
            raise ValueError("Invalid authorization type. Expected one of the following: %s" % cls.AUTH_OPTIONS)
        elif authorization == 'oauth1':
            auth = OAuth1(auth_data['application_key'], auth_data['application_secret'])
        elif authorization == 'basic':
            auth = HTTPBasicAuth(auth_data['username'], auth_data['password'])
        else:
            auth = None

        return auth
