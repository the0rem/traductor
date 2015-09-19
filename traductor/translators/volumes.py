from .base import BaseTranslator

class Volumes(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "-v %s" % " -v ".join(value)