from flask import Flask
from routes import user_routes
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(user_routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001)
