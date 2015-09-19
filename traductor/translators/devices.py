from traductor.translators.base import BaseTranslator

class Devices(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--device=[%s]" % ",".join(value)