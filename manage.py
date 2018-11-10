from popresearch.app import create_app
import os
from gevent.pywsgi import WSGIServer
from werkzeug.serving import run_with_reloader
from werkzeug.debug import DebuggedApplication


app = create_app()


@run_with_reloader
def run_server():
    if app.config.get('DEBUG', False):
        application = DebuggedApplication(app)
    else:
        application = app

    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '5000'))
    server = WSGIServer((host, port), application)
    server.serve_forever()

if __name__ == '__main__':
    run_server()
