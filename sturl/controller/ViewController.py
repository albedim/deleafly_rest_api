from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from sturl.service.UrlService import UrlService
from sturl.utils.Utils import Utils


url: Blueprint = Blueprint('UrlController', __name__, url_prefix=Utils.getURL('url'))

