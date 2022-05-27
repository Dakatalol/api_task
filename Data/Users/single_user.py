USER_ID_2 = {
    'INPUT_REQUEST_BODY':
        2
    ,
    'EXPECTED_RESPONSE_BODY': {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }

}

INVALID_USER = {
    'INPUT_REQUEST_BODY':
        2222222222
    ,
    # it returns empty response when user is not valid
    'EXPECTED_RESPONSE_BODY': {

    }
}
