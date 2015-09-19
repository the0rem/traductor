from traductor.translators.base import BaseTranslator

class Labels(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--label=[%s]" % ",".join(value)