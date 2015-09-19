from traductor.translators.base import BaseTranslator

class User(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "-u %s" % value