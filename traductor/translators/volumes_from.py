from .base import BaseTranslator

class VolumesFrom(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        return "--volumes-from=[%s]" % ",".join(value)