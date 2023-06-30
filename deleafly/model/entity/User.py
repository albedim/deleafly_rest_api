import datetime
from deleafly.configuration.config import sql


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class User(sql.Model):
    __tablename__ = 'users'
    user_id: int = sql.Column(sql.Integer, primary_key=True)
    password_forget_token: str = sql.Column(sql.String(40), nullable=True)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    created_on: datetime.date = sql.Column(sql.Date, nullable=True)
    complete_name = sql.Column(sql.String(40), nullable=False)

    def __init__(self, complete_name, email, password):
        self.email = email
        self.complete_name = complete_name
        self.password = password
        self.created_on = datetime.date.today()
        self.password_forget_token = True

    def toJson(self):
        return {
            'user_id': self.user_id,
            'complete_name': self.complete_name,
            'email': self.email,
            'created_on': self.created_on
        }