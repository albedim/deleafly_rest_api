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

    @classmethod
    def getUrls(cls, userId):
        return Utils.createSuccessResponse(True, {
            'max_urls': 5,
            'urls': Utils.createList(UrlRepository.getUrls(userId))
        })

    @classmethod
    def getUrl(cls, user, shortedUrl):
        url = UrlRepository.getUrlByCode(shortedUrl)
        if url is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        if user['user_id'] != url.user_id:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403
        return Utils.createSuccessResponse(True, url.toJson())

    @classmethod
    def removeUrl(cls, urlId):
        userId = UrlRepository.getUrl(urlId).user_id
        UrlRepository.removeUrl(urlId)
        return cls.getUrls(userId)

