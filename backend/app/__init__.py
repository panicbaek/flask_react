from flask import Flask, jsonify
from .extensions import db, migrate, login_manager, cors
from .config import Config
from .models import User
from flask_login import login_required # 로그인 안된사람은 접근 못하게하는 라이브러리

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config) # 환경설정에 필요한 값을 세팅한 클래스를 불러옴

  db.init_app(app)
  migrate.init_app(app, db)
  cors.init_app(app, origins=app.config['CORS_ORIGINS'], supports_credentials=True) # supports_credentials=True 크로스 오리진 요청에서 자격증명 관련된걸 주고받을 수 있도록 하겠다는 소리
                                                                                    # 서버에서 항상 쿠키 검사를 함
  login_manager.init_app(app)

# login_manager를 이용해서 로그인을 하면 기본키 id만 기억하고있다가 정보가 필요하면 user_loader로 정보를 받아올 수 있음 
  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(user_id)
  
# 인증되지 않은 사용자가 로그인을 요청할때 튕겨내는 함수
  @login_manager.unauthorized_handler
  def unauthorized():
    return jsonify({ 'ok' : False, 'message' : '인증되지 않은 사용자'}), 401
  
  from .blueprints.auth import bp as auth_bp
  from .blueprints.post import bp as post_bp

  app.register_blueprint(auth_bp, url_prefix='/auth')
  app.register_blueprint(post_bp, url_prefix='/post')

  @app.route('/check')
  def check():
    return {'ok' : True}

  @app.route('/check2')
  def check2():
    return {'ok' : True}

  return app