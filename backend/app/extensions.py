from flask_sqlalchemy import SQLAlchemy # DB 연결
from flask_migrate import Migrate # DB 수정
from flask_login import LoginManager # 로그인 매니저
from flask_cors import CORS # 프론트 벡엔드 주소 연결

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
cors = CORS()