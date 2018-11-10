import logging

try:
    import flask
    from .core import PRAPI
except:
    pass

__version__ = '0.0.1'

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
