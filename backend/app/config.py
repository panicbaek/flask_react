import os
import secrets

class Config:
  SECRET_KEY = secrets.token_urlsafe(32) #  웹 애플리케이션의 보안을 위해 사용되는 비밀 키를 설정합니다.
  SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI') # 애플리케이션이 연결할 데이터베이스의 주소(URI)를 설정합니다.
  SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy가 객체 수정 사항을 추적하는 기능을 비활성화합니다.
  SQLALCHEMY_ECHO = True # 애플리케이션이 데이터베이스에 실행하는 모든 SQL 문을 콘솔에 출력하도록 설정합니다.
  CORS_ORIGINS = ["http://localhost:5173"]  # 크로스 오리진에 허용할 주소세팅 