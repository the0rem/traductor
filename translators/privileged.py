from .base import BaseTranslator

class Privileged(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--privileged=%s" % value