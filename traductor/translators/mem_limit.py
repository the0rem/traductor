from .base import BaseTranslator

class MemLimit(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--memory=%s" % value