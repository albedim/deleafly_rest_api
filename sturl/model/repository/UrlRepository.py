import datetime

from sqlalchemy.sql.elements import or_

from sturl.configuration.config import sql
from sturl.model.entity.Url import Url


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
