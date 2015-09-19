from .base import BaseTranslator

class CpuShares(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--cpu-shares=%s" % value