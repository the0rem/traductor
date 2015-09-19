from .base import BaseTranslator

class EnvFile(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--env-file=[%s]" % ",".join(value)