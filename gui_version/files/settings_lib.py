import configparser


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Settings(Borg):
    def __init__(self, filename):
        Borg.__init__(self)
        self.filename = filename
        self.config_parser = configparser.ConfigParser()
        self.read_conf_file(self.config_parser, filename)
        self.remember_last_directory = self.str_to_bool(self.config_parser.get('General', 'remember_last_directory'))
        self.timer_window_settings = {}

        for key, val in self.config_parser.items('TimerWindowOptions'):
            try:
                val = float(val)
            except:
                pass
            self.timer_window_settings.update({key: val})

    def __str__(self):
        return str(self.__class__) + str(id(self))

    def save_config(self, filename=None):
        if filename is None: filename = self.filename
        else: self.filename = filename
        cfgfile = open(filename, 'w')
        self.config_parser.set("General", 'remember_last_directory', str(self.remember_last_directory))
        # print(dict(self.config_parser.items('General')))
        for key, val in self.timer_window_settings.items():
            self.config_parser.set("TimerWindowOptions", key, str(val))
        self.config_parser.write(cfgfile)
        cfgfile.close()

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
