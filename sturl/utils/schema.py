
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
]