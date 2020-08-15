from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
db=SQLAlchemy()
migrate=Migrate()
def create_app():
    app = Flask(__name__)
    #db url 불러와서 app 설정
    app.config.from_object(config)
    #db, migrate(수정) 시작
    from . import models
    db.init_app(app)
    migrate.init_app(app,db)
    # 블루프린트
    from .views import main_views,question_views,answer_views
    # 블루 프린트 등록(views)
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    return app