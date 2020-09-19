import os.path
import yaml
import logging
from shutil import copyfile

CONFIG = dict()

def check_configurations():
    yml_dir = f'{os.path.dirname(__file__)}/../configuration'
    yml_location = f"{yml_dir}/config.yml"
    if not os.path.exists(yml_dir):
        os.makedirs(yml_dir)
    if not os.path.isfile(yml_location):
        copyfile(rf'Template/config_template.txt', yml_location)
        print(
            'A configuration file configuration/config.yaml has been created. Please open it in a text editor, \
             \nfill out your configurations and restart the program. Consult the README for more information on the settings.')
        return False
    else:
        with open(yml_location, "r") as ymlfile:
            config_dict = yaml.load(ymlfile, Loader=yaml.FullLoader)
            if validate_config(config_dict):
                global CONFIG
                CONFIG = config_dict
                return True

def config():
    return CONFIG

def validate_config(dct):
    # bot token
    try:
        token = dct['bot']['token']
        if token == 'token123':
            return print(f"Please replace '{token}' in configuration/config.yml by the token of the Discord bot account,\nfill out the rest of your preferences, and restart the program. Consult the README.")

    except KeyError:
        return print(f"ERROR: configuration/config.yml doesn't contain the required setting for the bot token. Consult the README.")
    # multiple roles setting
    try:
        multiple_roles = dct['commands']['roles']['allow_adding_multiple_roles_at_once']
        if type(multiple_roles) != bool:
            return print(f"ERROR: The setting 'allow_adding_multiple_roles_at_once' has to be a bool.")
        if multiple_roles:
            try:
                max_roles = dct['commands']['roles']['max_roles_at_once']
                if type(max_roles) != int:
                    return print("ERROR: The 'max_roles_at_once' setting has to be an integer.")
                if max_roles < 1 or max_roles > 20:
                    return print("ERROR: The 'max_roles_at_once' setting has to be an integer between 1 and 20.")
            except KeyError:
                return print("ERROR: The setting 'max_roles_at_once' is required when 'allow_adding_multiple_roles_at_once' is set to True.")
    except KeyError:
        return print(f"ERROR: configuration/config.yml doesn't contain the required commands/roles setting 'allow_adding_multiple_roles_at_once'. Consult the README.")
    # command permissions
    for command in dct['commands'].keys():
        try:
            permission = dct['commands'][command]['permission']
            permission_values = ['above', 'below', 'anyone']
            if permission not in permission_values:
                return print(f"ERROR: The setting 'permission' can only have one of the following values: {permission_values}.")
        except KeyError:
            pass
    # logging
    try:
        logging_level = dct['logging']['level']
        if not type(logging.getLevelName(logging_level.upper())) == int:
            return print (f"ERROR: Invalid logging level '{logging_level}'.")
    except KeyError:
        pass
    return True

