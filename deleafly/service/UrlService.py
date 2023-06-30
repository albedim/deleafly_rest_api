from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from deleafly.model.entity.User import User
from deleafly.model.repository.UrlRepository import UrlRepository
from deleafly.model.repository.UserRepository import UserRepository
from deleafly.service.ViewService import ViewService
from deleafly.utils.Constants import Constants
from deleafly.utils.Utils import Utils


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
    def create(cls, request):
        if not Utils.isValid(request, "URL_CREATE"):
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 415), 415
        if UserRepository.getUserById(request['user_id']) is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        if len(UrlRepository.getUrls(request['user_id'])) == 5:
            return Utils.createWrongResponse(False, Constants.MAX_URLS_REACHED, 403), 403
        UrlRepository.create(
            request['original_url'],
            request['user_id'],
            request['name'],
            Utils.createLink(8)
        )
        return cls.getUrls(request['user_id'])

    @classmethod
    def getUrls(cls, userId):
        return Utils.createSuccessResponse(True, {
            'max_urls': 5,
            'urls': Utils.createListOfPages(Utils.createList(UrlRepository.getUrls(userId)), 3)
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
        ViewService.removeViews(urlId)
        return cls.getUrls(userId)

    @classmethod
    def update(cls, user, urlId, newName):
        url = UrlRepository.getUrl(urlId)
        if url is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        if user['user_id'] != url.user_id:
            return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 403), 403
        UrlRepository.update(url, newName)
        return cls.getUrls(url.user_id)

