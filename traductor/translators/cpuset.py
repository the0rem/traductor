from traductor.translators.base import BaseTranslator

class Cpuset(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--cpuset-cpus=%s" % value