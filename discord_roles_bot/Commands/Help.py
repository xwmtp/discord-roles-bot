from Commands.Command import Command
from Config import config
from Helpers import get_roles

class Roles(Command):

    def __init__(self):
        command_name = 'help'
        command_triggers = ['!roles', '!help']
        super().__init__(command_name, command_triggers)

class Help:

    async def get_response(self, message, bot):
        available_roles = get_roles(bot, message.guild, True)
        role_descriptions_dict, unused_roles = self.build_role_description_dict(available_roles)
        role_descriptions = self.role_descriptions_to_list(role_descriptions_dict)

        other_roles_str = '' if role_descriptions == '' else 'Other available roles: '

        response = f"```Use !add role or !remove role to add/remove roles. You can add multiple at once. Available roles:\n\n \
                     {role_descriptions}\n \
                     {other_roles_str}{', '.join(sorted(unused_roles))}```\
                   "
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
        max_role_len = len(max(dct.keys(), key=len))
        for role, description in dct.items():
            role_descriptions += f"{role}{' ' * max(0, max_role_len - len(role))} - {description}\n"
        return role_descriptions



