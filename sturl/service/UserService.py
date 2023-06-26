from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from sturl.model.entity.User import User
from sturl.model.repository.UserRepository import UserRepository
from sturl.service.UrlService import UrlService
from sturl.utils.Constants import Constants
from sturl.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#

class UserService():

    @classmethod
    def signin(cls, request: dict) -> tuple[Any, int] | Any:
        if not Utils.isValid(request, "SIGNIN_USER"):
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 415), 415
        user: User = UserRepository.signin(
            request['email'],
            Utils.hash(request['password'])
        )
        if user is not None:
            return Utils.createSuccessResponse(True, {
                "token": create_access_token(
                    identity=user.toJson(),
                    expires_delta=timedelta(weeks=4))
            })
        else:
            return Utils.createWrongResponse(False, Constants.USER_NOT_FOUND, 404), 404

    @classmethod
    def existsByEmail(cls, email) -> bool:
        return UserRepository.getUserByEmail(email) is not None

    @classmethod
    def getUserById(cls, userId):
        user: User = UserRepository.getUserById(userId)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            return user.toJson()

    @classmethod
    def signup(cls, request: dict):
        if not Utils.isValid(request, "SIGNUP_USER"):
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 415), 415
        if cls.existsByEmail(request['email']):
            return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
        else:
            user: User = UserRepository.signup(
                request['complete_name'],
                request['email'],
                Utils.hash(request['password']),
            )
            UrlService.createFirst(request['first_url'], user)
            return Utils.createSuccessResponse(True, {
                "token": create_access_token(
                    identity=user.toJson(),
                    expires_delta=timedelta(weeks=4))
            })

    @classmethod
    def createForgottenPasswordToken(cls, email):
        user: User = UserRepository.getUserByEmail(email)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            token: str = Utils.createLink(40)
            UserRepository.createForgottenPasswordToken(user, token)
            Utils.sendPasswordForgottenEmail(user.email, token)
            return Utils.createSuccessResponse(True, Constants.CREATED), 200

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = UserRepository.getUserByPasswordForgottenToken(token)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            return Utils.createSuccessResponse(True, user.user_id), 200

    @classmethod
    def changePassword(cls, request) -> tuple[Any, int] | dict:
        if not Utils.isValid(request, "CHANGE_PASSWORD"):
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 415), 415
        UserRepository.changePassword(request['user_id'], Utils.hash(request['new_password']))
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def sync(cls, requestUser):
        user = cls.getUserById(requestUser['user_id'])
        if user == requestUser:
            return Utils.createSuccessResponse(True, Constants.UP_TO_DATE)
        else:
            return Utils.createSuccessResponse(False, user)
