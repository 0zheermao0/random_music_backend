from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):  # 定义与表格对应的类，表与结构的名称均与mysql中一致
		# 表的名称
		__tablename__ = 'user'
		# 表的结构
		id = db.Column(db.Integer(), nullable=False, primary_key=True)
		phone = db.Column(db.String(20), nullable=False, unique=True)
		password = db.Column(db.String(20), nullable=False)
		username = db.Column(db.String(20), nullable=False)
		realname = db.Column(db.String(20), nullable=True)
		email = db.Column(db.String(20), nullable=True)

class Music(db.Model):
		__tablename__ = 'classic_music'
		id = db.Column(db.Integer(), nullable=False, primary_key=True)
		label = db.Column(db.String(255), nullable=True)
		artist = db.Column(db.String(255), nullable=True)
		src = db.Column(db.String(255), nullable=True)

		def __init__(self, label, artist, src):
				self.label = label
				self.artist = artist
				self.src = src
