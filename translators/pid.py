from .base import BaseTranslator

class Pid(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--pid=%s" % value