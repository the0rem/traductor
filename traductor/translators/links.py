from .traductor.translators.base import BaseTranslator

class Links(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--link=[%s]" % ",".join(value)