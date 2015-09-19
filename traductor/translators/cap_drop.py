from .base import BaseTranslator

class CapDrop(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--cap-drop=[%s]" % ",".join(value)