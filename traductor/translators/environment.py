from traductor.translators.base import BaseTranslator

class Environment(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        if type(value) is not dict and type(value) is not list:
            return ""

        environments = ""

        if type(value) is dict:
            for env_key, env_val in value.iteritems():
                environments += "-e %s:%s" % (env_key, env_val,)

        if type(value) is list:

        return "%s" % environments