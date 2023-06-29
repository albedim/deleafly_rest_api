from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from sturl.service.UserService import UserService
from sturl.utils.Utils import Utils


user: Blueprint = Blueprint('UserController', __name__, url_prefix=Utils.getURL('user'))


@user.route("/signin", methods=['POST'])
@cross_origin()
def signin():
    return UserService.signin(request.json)


@user.route("/password_forgotten_token/<email>", methods=['PUT'])
@cross_origin()
def createPasswordForgottenToken(email):
    return UserService.createForgottenPasswordToken(email)


@user.route("/password_forgotten_token/<token>", methods=['GET'])
@cross_origin()
def getUserByPasswordForgottenToken(token):
    return UserService.getUserByPasswordForgottenToken(token)


@user.route("/change_password", methods=['PUT'])
@cross_origin()
def changePassword():
    return UserService.changePassword(request.json)


@user.route("/signup", methods=['POST'])
@cross_origin()
def signup():
    return UserService.signup(request.json)


@user.route("/sync", methods=['GET'])
@cross_origin()
@jwt_required()
def sync():
    return UserService.sync(get_jwt_identity())


@user.route("/change/<userId>", methods=['PUT'])
@cross_origin()
def change(userId):
    return UserService.change(userId, request.json)


