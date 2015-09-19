from .traductor.translators.base import BaseTranslator

class Hostname(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--hostname=%s" % value