from .base import BaseTranslator

class CapAdd(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--cap-add=[%s]" % ",".join(value)
