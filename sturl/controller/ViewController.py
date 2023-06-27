from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from sturl.service.ViewService import ViewService
from sturl.utils.Utils import Utils


view: Blueprint = Blueprint('ViewController', __name__, url_prefix=Utils.getURL('view'))


@view.route("/get/<urlId>", methods=['GET'])
@cross_origin()
def getDailyView(urlId):
    return ViewService.get(urlId, request.args.get("mode"))
