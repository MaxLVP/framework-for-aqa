

class Singleton(type):

    """Singleton realization."""

    _instances = None

    def __call__(cls, *args, **kwargs):
        if not Singleton._instances:
            Singleton._instances = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances

    @staticmethod
    def get_instance():
        return Singleton._instances

