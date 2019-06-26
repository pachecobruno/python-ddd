from schematics.models import Model
from schematics.exceptions import DataError
from schematics.types import *


class GenericModel(Model):
    """
    GenericModel is an immutable data structure holding object
    """

    def is_valid(self):
        try:
            self.validate()
        except DataError:
            return False
        return True

    def validation_errors(self):
        try:
            self.validate()
            return None
        except Exception as e:
            return e

    def __repr__(self):
        return '<{}>({})'.format(type(self).__name__, self.__dict__['_data'])
