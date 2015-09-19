from traductor.translators.base import BaseTranslator

class Labels(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        labels = ""

        for label_key, label_val in value.iteritems():
            labels += " -l %s:%s" % (label_key, label_val,)

        return "%s" % labels