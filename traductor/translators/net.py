from traductor.translators.base import BaseTranslator

class Net(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--net=%s" % value