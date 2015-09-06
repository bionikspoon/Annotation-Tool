
# noinspection PyPep8Naming
class classproperty(object):
    """Decorator.  Define class property."""

    def __init__(self, attr):
        self.attr = attr

    def __get__(self, _, owner):
        return self.attr(owner)
