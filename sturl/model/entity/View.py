import datetime
from sturl.configuration.config import sql


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class View(sql.Model):
    __tablename__ = 'views'
    view_id: int = sql.Column(sql.Integer, primary_key=True)
    ip_address: str = sql.Column(sql.String, nullable=True)
    country: str = sql.Column(sql.String(40), nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)

    def __init__(self, ip_address, country):
        self.ip_address = ip_address
        self.country = country
        self.created_on = datetime.date.today()

    def toJson(self):
        return {
            'view_id': self.view_id,
            'ip_address': self.ip_address,
            'country': self.country,
            'created_on': self.created_on
        }