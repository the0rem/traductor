from .traductor.translators.base import BaseTranslator

class ContainerName(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--name=%s" % value