import discord
from Config import config
from Commands.Command import Command
from Helpers import find_string_match, get_kappa, get_roles

class Roles(Command):

    def __init__(self):
        command_name = 'roles'
        command_triggers = ['!add', '!remove']
        super().__init__(command_name, command_triggers)


    async def get_response(self, settings, message, bot):
        response = []

        words = message.content.split(' ')
        if len(words) <= 1:
            return 'Please add a role that you want added or removed'

        command = words[0]
        requested_roles = self.get_requested_roles(settings, words)

        available_roles = get_roles(bot, message.guild, True)
        unavailable_roles = get_roles(bot, message.guild, False)

        for requested_role in requested_roles:
            if find_string_match(requested_role, unavailable_roles):
                response.append(f'Nice try {get_kappa(message.guild)}')
                continue

            matching_role = find_string_match(requested_role, available_roles)
            if matching_role:
                role_response = await self.process_role(matching_role, command, message.author, message.guild)
                response.append(role_response)
            else:
                response.append(f"{message.author.mention} Invalid role `{requested_role}`, use `!roles` to see availables roles")

        return response

    def get_requested_roles(self, settings, words):
        if settings['commands'][self.name]['allow_adding_multiple_roles_at_once']:
            try:
                max_roles = settings['commands'][self.name]['max_roles_at_once']
            except KeyError:
                max_roles = 5
            return words[1:max_roles+1]
        else:
            return [' '.join(words[1:])]

    async def process_role(self, role, command, author, guild):
        try:
            if command == '!add':
                await author.add_roles(role)
                return f"Added role '{str(role)}' to {author.mention}"
            if command == '!remove':
                await author.remove_roles(role)
                return f"Removed role '{str(role)}' from {author.mention}"
        except discord.errors.Forbidden:
            return ("Nice try , that's forbidden" + get_kappa(guild))



