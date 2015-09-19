from .base import BaseTranslator

class Restart(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--restart=%s" % value
