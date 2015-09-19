from .traductor.translators.base import BaseTranslator

class Ports(BaseTranslator):
    """
    Port Mapping
    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "-p %s" % " -p ".join(value)