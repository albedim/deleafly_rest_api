from datetime import timedelta
from typing import Any
from flask_jwt_extended import create_access_token
from sturl.model.entity.User import User
from sturl.model.repository.ViewRepository import ViewRepository
from sturl.utils.Constants import Constants
from sturl.utils.Utils import Utils


class ViewService():

    @classmethod
    def get(cls, urlId, mode):
        obj = { }
        platformLabels = []
        platformValues = []
        countryLabels = []
        countryValues = []
        if mode == 'daily':
            views = ViewRepository.getDaily(urlId)
            platforms = ViewRepository.getDailyByPlatform(urlId)
            countries = ViewRepository.getDailyByCountry(urlId)
            obj = Constants.DAY_CHART_SCHEMA
            for view in views:
                obj[str(view[1]) + ":00" if int(view[1]) > 9 else "0" + str(view[1]) + ":00"] = view[0]
        elif mode == 'weekly':
            views = ViewRepository.getWeekly(urlId)
            platforms = ViewRepository.getMonthlyByPlatform(urlId)
            countries = ViewRepository.getWeeklyByCountry(urlId)
            obj = Constants.WEEK_CHART_SCHEMA
            for view in views:
                obj[str(view[1])] = view[0]
        elif mode == 'monthly':
            views = ViewRepository.getMonthly(urlId)
            platforms = ViewRepository.getMonthlyByPlatform(urlId)
            countries = ViewRepository.getMonthlyByCountry(urlId)
            obj = Constants.MONTH_CHART_SCHEMA
            for view in views:
                obj[str(view[1])] = view[0]
        for country in countries:
            countryLabels.append(Constants.COUNTRIES[country[1]])
            countryValues.append(country[0])
        for platform in platforms:
            platformLabels.append(platform[1])
            platformValues.append(platform[0])
        print(countries)
        return Utils.createSuccessResponse(True, {
            'views_chart': obj,
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
    def getByCountry(cls, urlId):
        views = ViewRepository.getDaily(urlId)
        labels = []
        values = []
        for view in views:
            labels.append(view[1])
            values.append(view[0])
        return Utils.createSuccessResponse(True, {
            'labels': labels,
            'values': values
        })