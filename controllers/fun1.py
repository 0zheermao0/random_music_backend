import os
import json
from models import User, Music, db
from flask import jsonify, current_app, request, abort
from utils import utils
from utils.redis_util import Redis
from utils.jwt_util import generate_access_token, generate_refresh_token, decode_auth_token, identify, login_required
import traceback
 
 
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']
        result = User.query.filter(User.phone == phone, User.password == password).one_or_none()
        if result:
            access_token = generate_access_token(user_name=phone)
            refresh_token = generate_refresh_token(user_name=phone)
            data = {"code": 200, 
                    "access_token": access_token, 
        			"refresh_token": refresh_token}
            return jsonify(data)
        else:
            return jsonify({'code': 401, 'message': 'login failed, no such user'})
    else:
        return jsonify({'code': 500, 'message': 'method invalid'})

def refresh():
    if request.method == 'POST':
        token = request.headers.get("Authorization", default=None)
        if not token:
            return jsonify(code=401, msg='not login')
        payload = decode_auth_token(token)
        if not payload:
            return jsonify(code=401, msg='not login')
        access_token = generate_access_token(user_name=phone)
        refresh_token = generate_refresh_token(user_name=phone)
        data = {"code": 200, 
                "access_token": access_token, 
        	    "refresh_token": refresh_token}
        return jsonify(data)
    else:
        return jsonify({'code': 500, 'message': 'method invalid'})
 
def register():
    current_app.logger.info("register")
    return 'this is register function'
 
 
def model_to_dict(result):  # 该函数用来将sqlalchemy的查询结果转为字典
    from collections import Iterable
    # 转换后，删除 '_sa_instance_state' 特殊属性
    try:
         if isinstance(result, Iterable):
             tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
             for t in tmp:
                 t.pop('_sa_instance_state')
         else:
             tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
             tmp.pop('_sa_instance_state')
         return tmp
    except BaseException as e:
        print(e)
 
 
 
def sql_query():  # 简单实现一个查询功能
    result = User.query.filter(User.id == 1).one_or_none()
    result_dict = model_to_dict(result)
    return jsonify(result_dict)

def get_song_amount():
	result = Music.query.all()
	data = {'amount': len(result)}
	return jsonify(data)
		

def get_song(query_id: int):
	result = Music.query.filter(Music.id == query_id).one_or_none()
	if result is None:
		return abort(404)
	print('music result', result)
	result_dict = model_to_dict(result)
	result_dict['src'] = current_app.config['MUSICSRC'] + result_dict['src']
	return jsonify(result_dict)

@login_required
def orderSongById(order_id: int):
	result = Music.query.filter(Music.id == order_id).one_or_none()
	if result is None:
		return jsonify({'code': 404, 'msg': 'no such song'})
	print('music result', result)
	result_dict = model_to_dict(result)
	result_dict['src'] = current_app.config['MUSICSRC'] + result_dict['src']
	try:
		Redis.write("orderSong", json.dumps(result_dict), 1*60*60)
	except Exception as e:
		traceback.print_exc()
		return jsonify({'code': 500, 'result': False})
	return jsonify({'code': 200, 'result': True})
	
def getOrderSong():
	result = Redis.read("orderSong")
	try:
		result = json.loads(result)
		return jsonify(result)
	except Exception as e:
		traceback.print_exc()
		return jsonify({'code': 500, 'message': "failed"})

def getSongByLbl(label: str):
	result = Music.query.filter(Music.label.like("%" + label + "%") if label is not None else "").all()
	data_list = []
	if result:
		for i in result:
			i_dict = model_to_dict(i)
			i_dict['src'] = current_app.config['MUSICSRC'] + i_dict['src']
			data_list.append(i_dict)
	return jsonify(data_list)

@login_required
def uploadMusic():
	if request.method == 'POST':
		label = request.form['label']
		artist = request.form['artist']
		upload_file = request.files['file']
		if upload_file:
			try:
					file_name = utils.getMd5(upload_file) + os.path.splitext(upload_file.filename)[-1]
					upload_file.seek(0)
					print(f'file name: {file_name}')
					save_path = os.path.join(current_app.config['UPLOADDIR'], file_name)
					print(f'save path: {save_path}')
					upload_file.save(save_path)
					upload_music = Music(label, artist, file_name)
					db.session.add(upload_music)
					db.session.commit()
			except Exception as e:
				traceback.print_exc()
				return jsonify({'code': 500, 'result': False})
		return jsonify({'code': 200, 'result': True})
