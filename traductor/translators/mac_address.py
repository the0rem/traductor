from .base import BaseTranslator

class MacAddress(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--mac-address=%s" % value