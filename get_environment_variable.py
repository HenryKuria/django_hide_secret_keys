import os
from django.core.exceptions import ImproperlyConfigured

def get_env_variable(name):
    """
    :param name:
    :return: environment variable
    """
    try:
        return os.environ.get(name)
    except KeyError:
        raise ImproperlyConfigured('Environment variable “{}” not found.'.format(name))
