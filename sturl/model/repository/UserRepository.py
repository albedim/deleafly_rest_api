import datetime

from sqlalchemy.sql.elements import or_

from sturl.configuration.config import sql
from sturl.model.entity.User import User


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class UserRepository():

    @classmethod
    def signin(cls, email, password) -> User:
        user: User = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def signup(cls, completeName, email, password) -> User:
        user: User = User(completeName, email, password)
        sql.session.add(user)
        sql.session.commit()
        return user

    @classmethod
    def getUserById(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def getUserByEmail(cls, email) -> User:
        user: User = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getAllUsers(cls) -> list:
        users: list = sql.session.query(User).all()
        return users

    @classmethod
    def createForgottenPasswordToken(cls, user, token) -> None:
        user.password_forget_token = token
        sql.session.commit()

    @classmethod
    def getUserByPasswordForgottenToken(cls, token) -> User:
        user: User = sql.session.query(User).filter(User.password_forget_token == token).first()
        return user

    @classmethod
    def changePassword(cls, userId, password) -> User:
        user: User = cls.getUserById(userId)
        user.password = password
        sql.session.commit()
