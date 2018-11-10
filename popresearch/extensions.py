import logging

logger = logging.getLogger(__name__)

try:
    from flask_sqlalchemy import SQLAlchemy
except:
    pgdb = None
else:
    pgdb = SQLAlchemy()

try:
    from flask_compress import Compress
except:
    zippy = None
else:
    zippy = Compress()
