import yaml

class SettingsManager:
    config_file_name = 'config.yaml'
    
    def __init__(self):
        print("コンストラクタ")
        with open(self.config_file_name) as file:
            self.config = yaml.safe_load(file.read())
        print(self.config)

    def __del__(self):
        # デストラクタ
        print("del:デストラクタ")

    def get_config(self):
        return self.config
    
    def set_config(self, input_config):
        self.config = input_config

    config = property(get_config, set_config)