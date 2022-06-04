from Utils.Utils import Utils

RANDOM_NEW_USER = {
    'INPUT_REQUEST_BODY':
        {
            "name": Utils().generate_random_name(),
            "job": Utils().generate_random_job()
        }
}
