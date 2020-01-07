from flask_login import current_user, login_user
from app import app, socketio
from app.models import User, Project

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@socketio.on('login')
def login(json):
    if current_user.is_authenticated:
        socketio.emit('rejected', 'You are already logged in')
    user = User.query.filter_by(email=json['mail']).first()
    if user is None or not user.check_password(json['password']):
        socketio.emit('rejected', 'Invalid username or password')
        return
    login_user(user)
    print(json['mail'], json['password'])