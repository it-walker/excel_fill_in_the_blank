from report_insured import ReportInsured
from settings_manager import SettingsManager

import os

def main():
    config_file_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    conf = SettingsManager()
    conf.load(config_file_path)
    report_instance = ReportInsured(conf)
    report_instance.generate()

if __name__ == '__main__':
    main()