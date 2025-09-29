from flask import Blueprint, request, jsonify
from email_validator import validate_email, EmailNotValidError # 이메일 유효성검사 해주는 라이브러리
from ..extensions import db
from ..models import User

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