import base64
import datetime
import hashlib
import io
import random
import smtplib
from email.message import EmailMessage
from flask import jsonify

from deleafly.utils.Constants import Constants
from resources.rest_service import config
from deleafly.utils.schema import SCHEMA


class Utils():

    @classmethod
    def createList(cls, elements):
        response = []
        for element in elements:
            response.append(element.toJson())
        return response

    @classmethod
    def createFreeList(cls, elements):
        response = []
        for element in elements:
            response.append(element)
        return response

    @classmethod
    def createSuccessResponse(cls, success, param):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "param": param,
            "code": 200,
        })

    @classmethod
    def createWrongResponse(cls, success, error, code):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "error": error,
            "code": code,
        })

    @classmethod
    def getURL(cls, controllerName):
        return '/api/v' + config['version'].split(".")[0] + '/' + controllerName

    @classmethod
    def hash(cls, password: str):
        return hashlib.md5(password.encode('UTF-8')).hexdigest()

    @classmethod
    def createLink(cls, length):
        letters = "ABCDEFGHILMNOPQRSTUVZYJKXabcdefghilmnopqrstuvzyjkx0123456789"
        link = ""
        for i in range(length):
            link += letters[random.randint(0, 59)]
        return link

    @classmethod
    def createCode(cls, length):
        letters = "ABCDEFGHILMNOPQRSTUVZYJKX0123456789"
        link = ""
        for i in range(length):
            link += letters[random.randint(0, 34)]
        return link

    @classmethod
    def sendExpireEmail(cls, user):
        msg = EmailMessage()
        msg.set_content("Hey " + user.username + ", your subscription is expired. remember to renew it not to lock your cryllinks")
        msg['Subject'] = "Cryllet - Subscription Expired"
        msg['From'] = Constants.EMAIL
        msg['To'] = user.email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Constants.EMAIL, Constants.PASSWORD)
        server.send_message(msg)
        server.quit()

    @classmethod
    def sendPasswordForgottenEmail(cls, email, token):
        msg = EmailMessage()
        msg.set_content(Constants.PASSWORD_FORGOTTEN_EMAIL.replace("{token}", token))
        msg['Subject'] = 'Cryllet - Forget password'
        msg['From'] = Constants.EMAIL
        msg['To'] = email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Constants.EMAIL, Constants.PASSWORD)
        server.send_message(msg)
        server.quit()

    @classmethod
    def decodeImage(cls, image, imageName):
        decodedImage = base64.b64decode(str(image))
        file = Image.open(io.BytesIO(decodedImage))
        file.save(imageName, 'png')

    @classmethod
    def encodeImage(cls, imageName):
        with open(imageName, "rb") as image:
            encodedImage = base64.b64encode(image.read())
        return str(encodedImage)

    @classmethod
    def isValid(cls, givenSchema, schemaName):
        for schema in SCHEMA:
            if schema['name'] == schemaName:
                for key in schema['schema']:
                    if key not in givenSchema or type(givenSchema[key]) != schema['schema'][key]:
                        return False
        return True

    @classmethod
    def createListOfPages(cls, array, pageLength):
        switchedElements = 0
        i = 0
        finalArray = []
        while len(array) != switchedElements:
            page = []
            for j in range(pageLength if len(array) - switchedElements > pageLength else len(array) - switchedElements):
                page.append(array[j + (i * pageLength)])
                switchedElements += 1
            i += 1
            finalArray.append(page)
        return finalArray

