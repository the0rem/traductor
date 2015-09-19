from .traductor.translators.base import BaseTranslator

class Tty(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "-t"