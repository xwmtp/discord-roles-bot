from Commands.Command import Command
from Config import config
from Helpers import get_roles

class Help(Command):

    def __init__(self):
        command_name = 'help'
        command_triggers = ['!roles', '!help']
        super().__init__(command_name, command_triggers)

    async def get_response(self, message, bot):
        available_roles = get_roles(bot, message.guild, True)
        role_descriptions_dict, unused_roles = self.build_role_description_dict(available_roles)
        role_descriptions = self.role_descriptions_to_list(role_descriptions_dict)

        other_roles_str = '' if role_descriptions == '' or unused_roles == [] else 'Other available roles: '
        if config()['commands']['roles']['allow_adding_multiple_roles_at_once']:
            max_roles = config()['commands']['roles']['max_roles_at_once']
            multiple_roles_str = f'You can add multiple at once (max {max_roles}), separated by spaces. '
        else:
            multiple_roles_str = ''

        response = f"```Use !add role or !remove role to add/remove roles. {multiple_roles_str}Available roles:\n\n" + \
                   role_descriptions + \
                   f"{other_roles_str}{', '.join(sorted(unused_roles))}```"
        return response

    def get_role_description(self, role):
        settings = config()
        if str(role) in settings['roles'] and 'description' in settings['roles'][str(role)].keys():
            return settings['roles'][str(role)]['description']


    def build_role_description_dict(self, available_roles):
        dct = {}
        unused_roles = []
        for role in available_roles:
            description = self.get_role_description(role)
            if description:
                dct[str(role)] = description
            else:
                unused_roles.append(str(role))

        return dct, unused_roles

    def role_descriptions_to_list(self, dct):
        role_descriptions = ''
        if dct:
            max_role_len = len(max(dct.keys(), key=len))
            for role, description in dct.items():
                role_descriptions += f"{role}{' ' * max(0, max_role_len - len(role))} - {description}\n"
        if role_descriptions != '':
            role_descriptions += '\n'
        return role_descriptions



