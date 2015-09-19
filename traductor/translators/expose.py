from .traductor.translators.base import BaseTranslator

class Expose(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--expose=[%s]" % ",".join(value)