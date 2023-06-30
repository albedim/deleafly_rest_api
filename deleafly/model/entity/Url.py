import datetime
from deleafly.configuration.config import sql


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class Url(sql.Model):
    __tablename__ = 'urls'
    url_id: int = sql.Column(sql.Integer, primary_key=True)
    user_id: str = sql.Column(sql.Integer, nullable=True)
    name: str = sql.Column(sql.String(40), nullable=False)
    shorted_url: str = sql.Column(sql.String(40), nullable=False)
    original_url: str = sql.Column(sql.String(1040), nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)

    def __init__(self, original_url, user_id, name, shorted_url):
        self.original_url = original_url
        self.user_id = user_id
        self.name = name
        self.created_on = datetime.date.today()
        self.shorted_url = shorted_url

    def toJson(self):
        return {
            'url_id': self.url_id,
            'user_id': self.user_id,
            'name': self.name,
            'shorted_url': self.shorted_url,
            'original_url': self.original_url,
            'created_on': self.created_on
        }