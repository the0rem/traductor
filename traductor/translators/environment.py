from traductor.translators.base import BaseTranslator

class Environment(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        environments = ""

        for env_key, env_val in value.iteritems():
            environments += "-e %s:%s" % (env_key, env_val,)

        return "%s" % environments