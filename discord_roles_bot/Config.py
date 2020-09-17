import os.path
import yaml
from shutil import copyfile

CONFIG = dict()

def valididate_config():
    yml_location = f'{os.path.dirname(__file__)}/../config.yml'
    if not os.path.isfile(yml_location):
        copyfile(rf'Template/config_template.txt', f'config.yml')
        print(
            'A configuration file config.yaml has been created in the root directory. Please open it in a text editor, \
             fill out your configurations and restart the program. Consult the README for more information on the settings.')
        return False
    else:
        with open(yml_location, "r") as ymlfile:
            global CONFIG
            CONFIG = yaml.load(ymlfile, Loader=yaml.FullLoader)
            return True

def config():
    return CONFIG

