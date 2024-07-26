from flask import Blueprint
from controllers.fun1 import login, register, sql_query
from flask_cors import CORS
from .music_routers import music_bp
 
# 创建蓝图
b1 = Blueprint('b1', __name__)
CORS(b1)  # 解决跨域问题
 
# 连接路由和相应函数
b1.route('/login', methods=['POST'])(login)
b1.route('/register', methods=['GET', 'POST'])(register)
b1.route('/mysqlquery', methods=['GET'])(sql_query)

# b1.route('/music/<int:query_id>', methods=['GET'])(get_song)
# b1.route('/music/amount', methods=['GET'])(get_song_amount)
# b1.route('/music/bylbl/<string:label>', methods=['GET'])(getSongByLbl)
# b1.route('/music/bylbl/<string:label>', methods=['GET'])(getSongByLbl)
# b1.route('/music/upload', methods=['POST'])(uploadMusic)
# 
# b1.route('/music/order/<int:order_id>', methods=['GET'])(orderSongById)
# b1.route('/music/getOrder', methods=['GET'])(getOrderSong)
