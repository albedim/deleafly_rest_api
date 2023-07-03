from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from deleafly.service.UrlService import UrlService
from deleafly.utils.Utils import Utils


url: Blueprint = Blueprint('UrlController', __name__, url_prefix=Utils.getURL('url'))


@url.route("/change/<urlId>", methods=['PUT'])
@cross_origin()
@jwt_required()
def update(urlId):
    return UrlService.update(get_jwt_identity(), urlId, request.args.get("name"))


@url.route("/get/of", methods=['GET'])
@cross_origin()
@jwt_required()
def getUrls():
    return UrlService.getUrls(get_jwt_identity())


@url.route("/get/<shortedUrl>", methods=['GET'])
@cross_origin()
@jwt_required()
def getUrlByCode(shortedUrl):
    return UrlService.getUrl(get_jwt_identity(), shortedUrl)


@url.route("/remove/<urlId>", methods=['DELETE'])
@cross_origin()
def removeUrl(urlId):
    return UrlService.removeUrl(urlId)


@url.route("/create", methods=['POST'])
@cross_origin()
def create():
    return UrlService.create(request.json)