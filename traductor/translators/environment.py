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
        env_dict = {}

        # Handle Dict Conversion
        if type(value) is dict:
            env_dict = value

        # Handle List Conversion
        if type(value) is list:
            first = True
            for env_pair in value:
                split = env_pair.split('=', 1)
                env_val = "";
                if len(split) > 0:
                    if len(split) > 1:
                        env_val = split[1]
                    env_dict[split[0]] = env_val

        # Convert to environments String
        first = True
        for env_key, env_val in env_dict.iteritems():
            if not first:
                environments += " "
            environments += "-e %s:%s" % (env_key, env_val,)
            if first:
                first = False

        return "%s" % environments