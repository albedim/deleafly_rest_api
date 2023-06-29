import datetime

from sqlalchemy import text
from sqlalchemy.sql.elements import or_

from sturl.configuration.config import sql
from sturl.model.entity.View import View


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 06/05/23
# Created at: 19:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class ViewRepository():

    @classmethod
    def getDaily(cls, urlId):
        views = sql.session.query(text('counter'), View.created_at).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, created_at "
                 "FROM views "
                 "WHERE created_on = CURDATE() "
                 "AND url_id = :urlId "
                 "GROUP BY created_at").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def getWeekly(cls, urlId):
        views = sql.session.query(text('counter'), View.created_on).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, "
                 "DAYNAME(created_on) "
                 "FROM views "
                 "WHERE YEARWEEK(created_on, 1) = YEARWEEK(CURDATE(), 1) "
                 "AND url_id = :urlId "
                 "GROUP BY created_on").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def getMonthly(cls, urlId):
        views = sql.session.query(text('counter'), View.created_on).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, MONTHNAME(created_on) "
                 "FROM views "
                 "WHERE DATE_SUB(NOW(), INTERVAL 1 MONTH) " 
                 "AND url_id = :urlId "
                 "GROUP BY "
                 "MONTH(created_on)").params(urlId = urlId)
        ).all()
        return views

    @classmethod
    def create(cls, urlId, platform, ipv4, countryCode):
        view = View(platform, urlId, ipv4, countryCode)
        sql.session.add(view)
        sql.session.commit()

    @classmethod
    def getDailyByCountry(cls, urlId):
        views = sql.session.query(text('counter'), View.country).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, country "
                 "FROM views "
                 "WHERE created_on = CURDATE() "
                 "AND url_id = :urlId "
                 "GROUP BY country").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def getWeeklyByCountry(cls, urlId):
        views = sql.session.query(text('counter'), View.country).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, "
                 "country "
                 "FROM views "
                 "WHERE YEARWEEK(created_on, 1) = YEARWEEK(CURDATE(), 1) "
                 "AND url_id = :urlId "
                 "GROUP BY country").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def getMonthlyByCountry(cls, urlId):
        views = sql.session.query(text('counter'), View.country).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, country "
                 "FROM views "
                 "WHERE DATE_SUB(NOW(), INTERVAL 1 MONTH) "
                 "AND url_id = :urlId "
                 "GROUP BY "
                 "country").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def getDailyByPlatform(cls, urlId):
        views = sql.session.query(text('counter'), View.platform).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, platform "
                 "FROM views "
                 "WHERE created_on = CURDATE() "
                 "AND url_id = :urlId "
                 "GROUP BY platform").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def getWeeklyByPlatform(cls, urlId):
        views = sql.session.query(text('counter'), View.platform).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, "
                 "platform "
                 "FROM views "
                 "WHERE YEARWEEK(created_on, 1) = YEARWEEK(CURDATE(), 1) "
                 "AND url_id = :urlId "
                 "GROUP BY platform").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def getMonthlyByPlatform(cls, urlId):
        views = sql.session.query(text('counter'), View.platform).from_statement(
            text("SELECT "
                 "COUNT(*) AS counter, platform "
                 "FROM views "
                 "WHERE DATE_SUB(NOW(), INTERVAL 1 MONTH) "
                 "AND url_id = :urlId "
                 "GROUP BY "
                 "platform").params(urlId=urlId)
        ).all()
        return views

    @classmethod
    def removeViews(cls, urlId):
        sql.session.query(View).filter(View.url_id == urlId).delete()
        sql.session.commit()