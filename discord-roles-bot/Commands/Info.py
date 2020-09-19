from Commands.Command import Command
from Helpers import find_string_match, get_roles

class Info(Command):

    def __init__(self):
        command_name = 'info'
        command_triggers = ['!info']
        super().__init__(command_name, command_triggers)

    async def get_response(self, message, bot):

        words = message.content.split(' ')

        if len(words) < 2:
            return "Please add a role you want info on"

        requested_info_role = words[1]

        available_roles = get_roles(bot, message.guild, True)

        if find_string_match(requested_info_role, available_roles):
            role_members = [member.name for member in message.guild.members if find_string_match(requested_info_role, member.roles)]
            members_str = f": {', '.join(sorted(role_members))}" if len(role_members) <= 100 else ''
            plural_str = '' if len(role_members) == 1 else 's'
            return f"Role '{requested_info_role}' has {len(role_members)} member{plural_str}{members_str}"
        else:
            return f"No info found for role '{requested_info_role}'"