import configparser


class Settings():
    def __init__(self, filename):
        config_parser = configparser.ConfigParser()
        self.read_conf_file(config_parser, filename)
        self.remember_last_directory = config_parser.get('General', 'remember_last_directory')
        self.timer_window_settings = {}

        for key, val in config_parser.items('TimerWindowOptions'):
            try:
                val = float(val)
            except:
                pass
            self.timer_window_settings.update({key: val})

    @staticmethod
    def read_conf_file(parser, filename):
        with open(filename) as f:
            parser.read_file(f)

    @staticmethod
    def set_settings(parser, filename):
        read_conf_file(parser, filename)
        self.remember_last_directory = parser.get('General', 'remember_last_directory')
