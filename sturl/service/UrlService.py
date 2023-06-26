from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from sturl.model.entity.User import User
from sturl.model.repository.UrlRepository import UrlRepository
from sturl.utils.Constants import Constants
from sturl.utils.Utils import Utils


class UrlService():

    @classmethod
    def createFirst(cls, original_url, user):
        UrlRepository.create(
            original_url,
            user.user_id,
            f"{user.complete_name.split(' ')[0]}'s First url",
            Utils.createLink(8)
        )

