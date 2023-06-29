
SCHEMA = [
    {
        "name": "SIGNIN_USER",
        "schema": {
            "email": str,
            "password": str
        }
    },
    {
        "name": "SIGNUP_USER",
        "schema": {
            "complete_name": str,
            "first_url": str,
            "email": str,
            "password": str
        }
    },
    {
        "name": "CHANGE_PASSWORD",
        "schema": {
            "user_id": int,
            "password": str
        }
    },
    {
        "name": "VIEW_CREATE",
        "schema": {
            "platform": str,
            "url_code": str,
            "ipv4": str,
            "country_code": str
        }
    },
    {
        "name": "URL_CREATE",
        "schema": {
            "user_id": int,
            "name": str,
            "original_url": str
        }
    },
    {
        "name": "CHANGE",
        "schema": {
            "complete_name": str,
            "new_password": str,
            "email": str
        }
    },
]