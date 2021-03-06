class CustomInt(int):
    """
    Make class for custom int, which will behave "vice versa" for comparison operations:
    e.g., int < int means less then, but custom int < int should equal custom int > int.
    Take into account <, >, >=, <=
    ** try to achieve this without __init__ rewriting
    """

    def __gt__(self, other):
        return False

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __ge__(self, other):
        return False


class PersonWithLimitedSkills:
    """
    Make class which is limited to 2 actions - eat and sleep
    Any other attributes addition should result in an error.
    """

    def __init__(self):
        self.__dict__['eat'] = 'eating'
        self.__dict__['sleep'] = 'sleeping'

    def __setattr__(self, name, value):
        if name in self.__dict__:
            super(PersonWithLimitedSkills, self).__setattr__(name, value)
        else:
            raise AttributeError(f"{self.__class__.__name__} has no attribute {name}")

    def eat(self):
        pass

    def sleep(self):
        pass


class HiddenAttrs:
    """
    Make class which never tells about its attributes.
    Its attribute list is always empty and attributes dictionary is always empty.
    """

    def __dir__(self):
        return []

    def __dict__(self):
        return {}


class CallableInstances:
    """
    Make class which takes func parameter on initialization, which is a callable that can be passed.
    Then object of this class may be called - callable passed on init will be called with passed parameters.
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, a):
        return self.func(a)
