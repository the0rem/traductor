from .base import BaseTranslator

class WorkingDir(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "-w %s" % value