from .error import PRConfigurationError


def init_settings(config):

    # postgres settings
    config.setdefault('DATABASE_URL', None)


def validate_settings(config):

    if config['SQLALCHEMY_DATABASE_URI'] in ('', None):
        raise PRConfigurationError(
            'Invalid SQLALCHEMY_DATABASE_URI value: {0}'
            .format(config['SQLALCHEMY_DATABASE_URI'])
        )
