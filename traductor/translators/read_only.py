from .base import BaseTranslator

class ReadOnly(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--read-only=%s" % value