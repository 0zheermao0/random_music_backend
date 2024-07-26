import os 
 
DEBUG = True
SECRET_KEY = os.urandom(24)
 
# DATABASE
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'music'
USERNAME = 'root'
PASSWORD = 'Mysql5.7'

# REDIS
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_EXPIRE = 60
 
 
URL = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(USERNAME,
                                                                PASSWORD,
                                                                HOSTNAME,
                                                                PORT,
                                                                DATABASE)
SQLALCHEMY_DATABASE_URI = URL
SQLALCHEMY_TRACK_MODIFICATIONS = False    

MUSICSRC = 'http://39.105.29.195:5001/music/'
UPLOADDIR = '/root/music/music/teenager_group/'
SECRET_KEY = 'iU116/J6kYiwPqEVpmhhAikOw/Q='
