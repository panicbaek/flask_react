from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from ..extensions import db
from ..models import Post

bp = Blueprint('post', __name__)

@bp.post('')
@login_required
def create_post():
  data = request.get_json()

  title = data.get('title')
  content = data.get('content')

  if not title or not content:
    return jsonify({'ok':False, 'message' : '제목, 내용을 작성해주세요'}), 400
  
  post = Post(title=title, content=content, author_id=current_user.id)

  db.session.add(post)
  db.session.commit()

  return jsonify({'ok':True, 'message':'게시글 등록 완료'}), 200

@bp.get('')
def post_list():
  posts = db.session.query(Post).order_by(Post.created_at.desc()).all()
  print(posts)
  print(type(posts))

  return jsonify({
     'ok' : True, 
     'posts' : [ post.to_dict() for post in posts ]
     })