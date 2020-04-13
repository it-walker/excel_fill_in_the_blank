import yaml

class SettingsManager:
    
    _section_in_out = 'in_out'
    _key_input_file_path = 'input_file_path'
    _key_template_file_path = 'template_file_path'
    _key_save_directory = 'save_directory'
    _key_save_file_name = 'save_file_name'

    @property
    def input_file_path(self):
        return self._input_file_path
    
    @property
    def template_file_path(self):
        return self._template_file_path
    
    @property
    def save_directory(self):
        return self._save_directory

    @property
    def save_file_name(self):
        return self._save_file_name

    def __init__(self):
        self._input_file_path = ''
        self._template_file_path = ''
        self._save_directory = ''
        self._save_file_name = ''

    def load(self, yaml_path):
        """設定ファイルを読み込みます
        
        Arguments:
            yaml_path {string} -- 設定ファイル（config.yaml）
        """        
        try:
            with open(yaml_path,"r", encoding="utf-8") as f:
                y = yaml.load(stream=f, Loader=yaml.SafeLoader)
                self._input_file_path = y[self._section_in_out][self._key_input_file_path]
                self._template_file_path = y[self._section_in_out][self._key_template_file_path]
                self._save_directory = y[self._section_in_out][self._key_save_directory]
                self._save_file_name = y[self._section_in_out][self._key_save_file_name]
        except:
            print("error", yaml_path)
            raise

