from flask_jwt_extended import JWTManager

from sturl.configuration.config import app, sql
from sturl.controller import UserController, UrlController

# controllers init
app.register_blueprint(UrlController.url)
app.register_blueprint(UserController.user)

# modules init
JWTManager(app)


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == '__main__':
    create_app().run()