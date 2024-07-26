import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing

# debug = True
bind = "0.0.0.0:8091"
pidfile = "/root/flaskMusic/logs/gunicorn.pid"
accesslog = "/root/flaskMusic/logs/gaccess.log"
errorlog = "/root/flaskMusic/logs/gdebug.log"
loglevel = 'info'
capture_output = True
daemon = True

# 启动的进程数
workers = 1
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'
