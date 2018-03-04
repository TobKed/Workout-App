import configparser


class Settings():
    def __init__(self, filename):
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
