from .base import BaseTranslator

class Entrypoint(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--entrypoint=%s" % value