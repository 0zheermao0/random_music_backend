from flask import Blueprint
from controllers.fun1 import get_song, get_song_amount, getSongByLbl, uploadMusic, orderSongById, getOrderSong
from flask_cors import CORS

music_bp = Blueprint('music', __name__)
CORS(music_bp)

music_bp.route('/music/<int:query_id>', methods=['GET'])(get_song)
music_bp.route('/music/amount', methods=['GET'])(get_song_amount)
music_bp.route('/music/bylbl/<string:label>', methods=['GET'])(getSongByLbl)
music_bp.route('/music/bylbl/<string:label>', methods=['GET'])(getSongByLbl)
music_bp.route('/music/upload', methods=['POST'])(uploadMusic)

music_bp.route('/music/order/<int:order_id>', methods=['GET'])(orderSongById)
music_bp.route('/music/getOrder', methods=['GET'])(getOrderSong)
