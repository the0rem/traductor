from .traductor.translators.base import BaseTranslator

class StdinOpen(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "-i"