from Commands.Command import Command
from Helpers import find_string_match, get_roles

class Info(Command):

    def __init__(self):
        command_name = 'info'
        command_triggers = ['!info']
        super().__init__(command_name, command_triggers)

    async def get_response(self, message, bot):

        requested_info_role = message.content.split(' ')[1]

        available_roles = get_roles(bot, message.guild, True)

        if find_string_match(requested_info_role, available_roles):
            role_members = [member.name for member in message.guild.members if find_string_match(requested_info_role, member.roles)]
            return f"Role '{requested_info_role}' has {len(role_members)} members: {', '.join(sorted(role_members))}"
        else:
            return f"No info found for role '{requested_info_role}'"