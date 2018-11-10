from .settings import init_settings, validate_settings


class PRAPI(object):
    """ Initialize the extension

        ARGS:
            app: the flask application
    """

    def __init__(self, app=None, config_type='default'):
        self.app = app

        if self.app is not None:
            self.init_app(app, config_type)

    def init_app(self, app, config_type):
        """ initialize the extension """

        # add default settings
        init_settings(app.config)

        # validate settings
        validate_settings(app.config)

        from .api.blueprint import bp
        app.register_blueprint(bp)

        self.app = app
        
