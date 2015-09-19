from .base import BaseTranslator

class DnsSearch(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--dns-search=[%s]" % " -p ".join(value)