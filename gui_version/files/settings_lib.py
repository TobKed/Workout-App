import configparser


class Borg:
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state


class Settings(Borg):
    def __init__(self, filename):
        Borg.__init__(self)
        config_parser = configparser.ConfigParser()
        self.read_conf_file(config_parser, filename)
        self.remember_last_directory = self.str_to_bool(config_parser.get('General', 'remember_last_directory'))
        self.timer_window_settings = {}

        for key, val in config_parser.items('TimerWindowOptions'):
            try:
                val = float(val)
            except:
                pass
            self.timer_window_settings.update({key: val})

    def __str__(self):
        return str(self.__class__) + str(id(self))

    @staticmethod
    def str_to_bool(tmp):
        if tmp == "True":
            return True
        elif tmp == "False":
            return False
        else:
            return None

    @staticmethod
    def read_conf_file(parser, filename):
        with open(filename) as f:
            parser.read_file(f)
