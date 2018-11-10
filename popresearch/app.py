import gevent.monkey
gevent.monkey.patch_all()

from psycogreen.gevent import patch_psycopg
patch_psycopg()

import logging
import logging.config
import os
import yaml

from .config import CONFIG_TYPE
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from .extensions import zippy, pgdb
from .core import PRAPI

logger = logging.getLogger(__name__)


def setup_logging(
    default_path='logging-config.yaml',
    default_level=logging.INFO,
    custom_logging_config='CUSTOM_LOGGING_CONFIG'
):
    """ setup logging configuration """
    logging_config_path = default_path
    custom_logging_path = os.getenv(custom_logging_config, None)
    if custom_logging_path:
        logging_config_path = custom_logging_path
    if os.path.exists(logging_config_path):
        with open(logging_config_path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.distConfig(config)
    else:
        logging.basicConfig(level=default_level)


def get_config_from_env():
    config_name = os.getenv('CONFIG_TYPE', 'default')
    return CONFIG_TYPE[config_name]


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(get_config_from_env())

    # configure logging
    setup_logging()

    # add the postgres connection
    pgdb.init_app(app)
    pgdb.app = app

    PRAPI(app)

    zippy.init_app(app)

    return app
