import ast
import datetime
import json
from datetime import timedelta
from typing import Any

from flask import jsonify
from flask_jwt_extended import create_access_token
from deleafly.model.entity.User import User
from deleafly.model.repository.UrlRepository import UrlRepository
from deleafly.model.repository.ViewRepository import ViewRepository
from deleafly.utils.Constants import Constants
from deleafly.utils.Utils import Utils


class ViewService():

    @classmethod
    def get(cls, urlId, mode):
        obj = {}
        viewsCounter = 0
        reviewsCounter = 0
        platformLabels = []
        platformValues = []
        countryLabels = []
        countryValues = []

        """ Views handlers """
        if mode == 'daily':
            views = ViewRepository.getDaily(urlId)
            platforms = ViewRepository.getDailyByPlatform(urlId)
            countries = ViewRepository.getDailyByCountry(urlId)
            reviewsCounter = ViewRepository.getDailyReviews(urlId)
            obj = Constants.DAY_CHART_SCHEMA.copy()
            for view in views:
                obj[str(view[1]) if int(view[1][:-3]) > 9 else "0" + str(view[1])] = view[0]
                viewsCounter += view[0]
        elif mode == 'weekly':
            views = ViewRepository.getWeekly(urlId)
            platforms = ViewRepository.getWeeklyByPlatform(urlId)
            countries = ViewRepository.getWeeklyByCountry(urlId)
            reviewsCounter = ViewRepository.getWeeklyReviews(urlId)
            obj = Constants.WEEK_CHART_SCHEMA.copy()
            print(obj)
            for view in views:
                obj[str(view[1])] = view[0]
                viewsCounter += view[0]
            print(obj)
        elif mode == 'monthly':
            views = ViewRepository.getMonthly(urlId)
            platforms = ViewRepository.getMonthlyByPlatform(urlId)
            countries = ViewRepository.getMonthlyByCountry(urlId)
            reviewsCounter = ViewRepository.getMonthlyReviews(urlId)
            obj = Constants.MONTHLY_CHART_SCHEMA().copy()
            month = str(datetime.datetime.now().month)
            for view in views:
                obj[str(view[1])+"/"+month if view[1] > 9 else "0"+str(view[1])+"/"+month] = view[0]
                viewsCounter += view[0]
        elif mode == 'yearly':
            views = ViewRepository.getYearly(urlId)
            platforms = ViewRepository.getYearlyByPlatform(urlId)
            countries = ViewRepository.getYearlyByCountry(urlId)
            reviewsCounter = ViewRepository.getYearlyReviews(urlId)
            obj = Constants.YEARLY_CHART_SCHEMA.copy()
            for view in views:
                obj[str(view[1])] = view[0]
                viewsCounter += view[0]
        else:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 415), 415
        """ countries handler """
        for country in countries:
            countryLabels.append(Constants.COUNTRIES[country[1]])
            countryValues.append(country[0])
        """ platform handler """
        for platform in platforms:
            platformLabels.append(platform[1])
            platformValues.append(platform[0])
        
        return Utils.createSuccessResponse(True, {
            'general': {
                'views': viewsCounter,
                'reviews': cls.reviewsAvarage(reviewsCounter)
            },
            'views_chart': {
               'value': obj
            },
            'countries_chart': {
               'labels': countryLabels,
               'values': countryValues
            },
            'platforms_chart': {
               'labels': platformLabels,
               'values': platformValues
            }
        })

    @classmethod
    def add(cls, request):
        if not Utils.isValid(request, "VIEW_CREATE"):
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 415), 415
        url = UrlRepository.getUrlByCode(request['url_code'])
        ViewRepository.create(
            url.url_id,
            request['platform'],
            request['ipv4'],
            request['country_code']
        )
        return Utils.createSuccessResponse(True, url.toJson())

    @classmethod
    def removeViews(cls, urlId):
        ViewRepository.removeViews(urlId)
        return Utils.createSuccessResponse(True, Constants.CREATED)

    @classmethod
    def reviewsAvarage(cls, array):
        totalsum = 0
        for e in array:
            totalsum += e[0]
        return 0 if len(array) == 0 else totalsum / len(array)

