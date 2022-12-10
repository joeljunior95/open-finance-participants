from src import app
from datetime import datetime
from gevent.pywsgi import WSGIServer

print(f"Starting server at {datetime.now()}")

http_server = WSGIServer(('0.0.0.0', 3000),app)
http_server.serve_forever()