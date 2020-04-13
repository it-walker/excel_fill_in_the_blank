import os
import tempfile
import yaml

import pytest

from settings_manager import SettingsManager


class TestSettingManager:

    def sample_config(self):
        return {'in_out': {'input_file_path': 'input',
                           'template_file_path': 'template',
                           'save_directory': 'save',
                           'save_file_name': 'file'}}

    def test_get_config(self):
        with tempfile.TemporaryDirectory() as dname:
            print(dname)                 # /tmp/tmpl2cvqpq5
            test_yaml = os.path.join(dname, "test.yaml")
            with open(test_yaml, "w") as f:
                yaml.dump(self.sample_config(), f)

                conf = SettingsManager()
                conf.load(test_yaml)
                assert conf.input_file_path == 'input'
                assert conf.template_file_path == 'template'
                assert conf.save_directory == 'save'
                assert conf.save_file_name == 'file'
