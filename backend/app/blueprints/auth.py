from flask import Blueprint, request, jsonify # 응답 관련 함수
from email_validator import validate_email, EmailNotValidError # 이메일 유효성검사 해주는 라이브러리
from ..extensions import db
from ..models import User
from flask_login import login_user, login_required, current_user, logout_user # login 관련 함수

#  애플리케이션 모듈화: 블루프린트는 관련된 기능들을 하나의 독립적인 모듈로 묶어줍니다.
#  예를 들어, 사용자 인증(회원가입, 로그인), 관리자 페이지, 상품 관리 등 기능별로 블루프린트를 만들 수 있습니다.

bp = Blueprint('auth', __name__)

@bp.post('/signup')
def signup():
  data = request.get_json()

  username = data.get('username')
  password = data.get('password')
  email = data.get('email')
  nickname = data.get('nickname')

  if not username or not password or not email:
    return jsonify({ 'ok' : False, 'message' : "아이디,비번,이메일은 필수입니다." }), 400
  
  try:
    validate_email(email) # 유효성 검사를 하다가 메일형식에 맞지 않으면 예외발생 시킴
  except EmailNotValidError as e :
    return jsonify({ 'ok':False, 'message': str(e) }), 400 # str(e) error메세지를 문자열로 변환후 응답
  except Exception: # ValidError에서 오류처리가 안된 오류는 여기로 보내짐
    return jsonify({ 'ok':False, 'message' : '알수 없는 이유로 인한 오류 발생'}), 400
  
  user = User(username=username, email=email, nickname=nickname) # 비밀번호를 제외한 user객체 생성
  user.set_password(password)

  db.session.add(user)
  
  # 중복된 아이디, 이메일 유효성검사
  try:
    db.session.commit()
  except Exception:
    db.session.rollback()
    return jsonify({'ok':False, 'message':'이미 등록된 아이디, 이메일입니다.'}), 400
  
  return jsonify({'ok':True, 'message':'회원 가입 완료', 'user':user.to_dict()}), 200

@bp.post('/login')
def login(): # 1. 프론트에서 정보받음, 2. 정보 검사, 3. 문제없으면 응답처리
  data = request.get_json() # 1. 프론트에서 받은 정보를 data변수에 담음

  username = data.get('username')
  password = data.get('password')

  if not username or not password: # 2. 정보 검사
    return jsonify({'ok':False, 'message':'아이디 또는 비밀번호를 입력해 주세요'}), 400
  
  # 사용자가 입력한 username에 해당하는 레코드를 DB에서 꺼내옴
  user = db.session.query(User).filter(User.username == username).first()
  
  # 꺼내왔는데 없을 수 있고 -> username이 잘못입력 and 있으면 -> 비번검사
  if not user or not user.check_password(password):
    return jsonify({'ok':False, 'message':'아이디 또는 비밀번호를 다시 입력해 주세요'}), 400
  
  # 3. 문제없으면 응답처리
  login_user(user) # login_user함수는 서버 세션에 user정보를 저장 시키는 함수
  return jsonify({'ok':True, 'message':'로그인 성공', 'user':user.to_dict()})

@bp.get('/me')
def me():
  if current_user.is_authenticated:
    return jsonify({ 'ok':True, 'user':current_user.to_dict()}), 200
  return jsonify({ 'ok':False, 'user': None}), 200

@bp.post('/logout')
@login_required
def logout():
  logout_user()
  return jsonify({ 'ok':True, 'messsage': '로그아웃 성공'}), 200