import datetime

from sqlalchemy.sql.elements import or_

from deleafly.configuration.config import sql
from deleafly.model.entity.Url import Url


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class UrlRepository():

    @classmethod
    def create(cls, original_url, user_id, name, shorted_url):
        url: Url = Url(original_url, user_id, name, shorted_url)
        sql.session.add(url)
        sql.session.commit()

    @classmethod
    def getUrls(cls, userId):
        urls: list[Url] = sql.session.query(Url).filter(Url.user_id == userId).all()
        return urls

    @classmethod
    def getUrl(cls, urlId):
        url = sql.session.query(Url).filter(Url.url_id == urlId).first()
        return url

    @classmethod
    def getUrlByCode(cls, urlCode):
        url = sql.session.query(Url).filter(Url.shorted_url == urlCode).first()
        return url

    @classmethod
    def removeUrl(cls, urlId):
        sql.session.query(Url).filter(Url.url_id == urlId).delete()
        sql.session.commit()

    @classmethod
    def update(cls, url, newName):
        url.name = newName
        sql.session.commit()
