from .base import BaseTranslator

class Dns(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--dns=[%s]" % " -p ".join(value)