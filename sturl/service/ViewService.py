import ast
import json
from datetime import timedelta
from typing import Any

from flask import jsonify
from flask_jwt_extended import create_access_token
from sturl.model.entity.User import User
from sturl.model.repository.UrlRepository import UrlRepository
from sturl.model.repository.ViewRepository import ViewRepository
from sturl.utils.Constants import Constants
from sturl.utils.Utils import Utils


class ViewService():

    @classmethod
    def get(cls, urlId, mode):
        obj = {}
        viewsLabel = 0
        platformLabels = []
        platformValues = []
        countryLabels = []
        countryValues = []

        """ Views handlers """
        if mode == 'daily':
            views = ViewRepository.getDaily(urlId)
            platforms = ViewRepository.getDailyByPlatform(urlId)
            countries = ViewRepository.getDailyByCountry(urlId)
            obj = Constants.DAY_CHART_SCHEMA.copy()
            for view in views:
                obj[str(view[1]) if int(view[1][:-3]) > 9 else "0" + str(view[1])] = view[0]
                viewsLabel += view[0]
        elif mode == 'weekly':
            views = ViewRepository.getWeekly(urlId)
            platforms = ViewRepository.getMonthlyByPlatform(urlId)
            countries = ViewRepository.getWeeklyByCountry(urlId)
            obj = Constants.WEEK_CHART_SCHEMA.copy()
            print(obj)
            for view in views:
                obj[str(view[1])] = view[0]
                viewsLabel += view[0]
            print(obj)
        elif mode == 'monthly':
            views = ViewRepository.getMonthly(urlId)
            platforms = ViewRepository.getMonthlyByPlatform(urlId)
            countries = ViewRepository.getMonthlyByCountry(urlId)
            obj = Constants.MONTH_CHART_SCHEMA.copy()
            for view in views:
                obj[str(view[1])] = view[0]
                viewsLabel += view[0]
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
               'views_chart': {
                   'label': viewsLabel,
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
