def api_route(self, *args, **kwargs):
    """ function to allow a flask restful instance to add routes
        using a decorator
    """

    def wrapper(cls):
        self.add_resource(cls, *args, **kwargs)
        return cls
    return wrapper
